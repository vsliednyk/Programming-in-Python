"""Main loop of our simulation"""

import logging

from config import load_config, parse_arguments
from logger import setup_logger
from save import save_alive, save_positions
from sheep import Sheep
from wolf import Wolf


def pack_history(
    position_history: list, round_index, wolf: Wolf, sheep_list: list[Sheep]
):
    position_history.append(
        {
            "round_no": round_index,
            "wolf_pos": (wolf.pos_x, wolf.pos_y),
            "sheep_pos": [
                (sheep.pos_x, sheep.pos_y) if sheep.is_alive() else None
                for sheep in sheep_list
            ],
        }
    )


def simulate():
    
    args = parse_arguments()
    setup_logger(args.log)

    position_history = []
    alive_history = []

    config = load_config(args.config)
    amount_of_sheep = args.sheep
    max_rounds = args.rounds
    wait = args.wait

    amount_alive = amount_of_sheep

    list_of_sheep = [
        Sheep(i, config["Sheep"]["InitPosLimit"], config["Sheep"]["MoveDist"])
        for i in range(amount_of_sheep)
    ]
    logging.info("All sheep initial positions were determined")

    wolf = Wolf((0, 0), config["Wolf"]["MoveDist"])
    round_index = 1
    logging.debug("Simulation has started")
    while round_index <= max_rounds and amount_alive > 0:
        logging.info("Round %s started", round_index)
        alive_sheep = [sheep for sheep in list_of_sheep if sheep.is_alive()]
        for sheep in alive_sheep:
            sheep.move_randomly()
        logging.info("All alive sheep moved")

        result = wolf.try_catching(list_of_sheep=alive_sheep)

        if result["result"] == "eaten":
            amount_alive -= 1

        show_round_summary(
            round_index,
            amount_alive,
            wolf.pos_x,
            wolf.pos_y,
            status=result["result"],
            sheep_id=result["sheep_id"],
        )

        pack_history(position_history, round_index, wolf, list_of_sheep)
        alive_history.append((round_index, amount_alive))

        save_positions(position_history=position_history)
        logging.debug("Positions saved to pos.json")

        save_alive(alive_history)
        logging.debug("Alive sheep counts saved to alive.csv")
        logging.info(f"Round {round_index} ended! Sheep alive: {amount_alive}")
        round_index += 1
        if wait:
            input("Press Enter to continue...")
    if amount_alive == 0:
        cause = "all sheep have been eaten"
    else:
        cause = "maximum number of rounds has been reached"
    logging.info(f"Simulation ended due to: {cause}")


def show_round_summary(
    round_index, amount_alive, wpos_x, wpos_y, status, sheep_id
):
    print()
    print(f"=== Round no. {round_index} ===")
    print(f"Amount of sheep left: {amount_alive}")
    print(f"Wolf's position is: ({wpos_x:.3f}, {wpos_y:.3f})")

    if status == "eaten":
        print(f"Sheep {sheep_id} was eaten")
    elif status == "chasing":
        print(f"Wolf is chasing sheep {sheep_id}")
    else:
        print("No sheep in sight.")


if __name__ == "__main__":
    simulate()
