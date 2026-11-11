"""Main loop of our simulation"""

from typing import Dict, Tuple, TypeAlias, TypedDict
from Wolf import Wolf
from Sheep import Sheep

from save import save_alive, save_positions

""" Expects:
    - config:{
        "Sheep":{
            "InitPosLimit"  :   float,
            "MoveDist"      :   float
            },
        "Wolf":{
            "MoveDist" : float
                }
            }"""


SheepConfigType: TypeAlias = Dict[str, float]
WolfConfigType: TypeAlias = Dict[str, float]
ConfigType: TypeAlias = Dict[str, SheepConfigType | WolfConfigType]


def pack_alive_sheep(sheep_list: list[Sheep]):
    list = []
    list.append((sheep.pos_x, sheep.pos_y) for sheep in sheep_list)
    return list


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
    return position_history


def simulate():
    position_history = []
    config = {
        "Sheep": {"InitPosLimit": 10.0, "MoveDist": 1.0},
        "Wolf": {"MoveDist": 30},
    }
    amount_of_sheep = 10
    max_rounds = 50
    preset = []
    alive_sheep = []
    wait = True  #
    # params

    amount_alive = amount_of_sheep
    list_of_sheep = []

    if preset:
        list_of_sheep = preset
        alive_sheep = [sheep for sheep in list_of_sheep if sheep.is_alive()]
        amount_alive = len(alive_sheep)
    else:
        list_of_sheep = [
            Sheep(i, config["Sheep"]["InitPosLimit"], config["Sheep"]["MoveDist"])
            for i in range(amount_of_sheep)
        ]

    wolf = Wolf((0, 0), config["Wolf"]["MoveDist"])
    round_index = 1

    while round_index <= max_rounds and amount_alive > 0:
        alive_sheep = [sheep for sheep in list_of_sheep if sheep.is_alive()]
        for sheep in alive_sheep:
            sheep.move_randomly()

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

        position_history = pack_history(
            position_history, round_index, wolf, list_of_sheep
        )
        save_positions(position_history=position_history)
        round_index += 1
        if wait:
            input("Press Enter ↲ to continue...")
    if amount_alive > 0:
        alive_sheep = [sheep for sheep in list_of_sheep if sheep.is_alive()]
        list_to_save = pack_alive_sheep(alive_sheep)
        save_alive(list_to_save)
    return 0


def show_round_summary(round_index, amount_alive, wpos_x, wpos_y, status, sheep_id):
    print()
    print(f"=== Round no. {round_index} ===")
    print(f"Amount of sheep left:{amount_alive}")
    print(f"Wolf's position is: ({wpos_x:.3f},{wpos_y:.3f})")
    if status == "eaten":
        print(f"Sheep {sheep_id} was eaten")
    elif status == "chasing":
        print(f"Wolf is chasing sheep {sheep_id}")
    else:
        print("No sheep in sight.")
    pass


if __name__ == "__main__":
    simulate()
    print()
