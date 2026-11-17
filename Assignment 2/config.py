import argparse
import configparser
import logging


def positive_int(number):
    number = int(number)
    if number > 0:
        return number
    raise argparse.ArgumentTypeError(f"{number} is not a positive integer")


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="Wolf-Sheep simulation",
        description="Simulation involving a wolf that tries "
        "to catch sheep scattered in a meadow",
    )
    parser.add_argument("-c", "--config", type=str, help="configuration file")

    log_choices = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    parser.add_argument(
        "-l", "--log", type=str, choices=log_choices, help="set the logging level"
    )

    parser.add_argument(
        "-r", "--rounds", type=positive_int, default=50, help="number of rounds"
    )

    parser.add_argument(
        "-s", "--sheep", type=positive_int, default=15, help="sheep amount"
    )

    parser.add_argument(
        "-w", "--wait", action="store_true", help="wait for input between rounds"
    )

    return parser.parse_args()


def load_config(filename):
    if filename is None:
        logging.debug("No config file given.")
        logging.debug(
            'Using default config: config={"Sheep": {"InitPosLimit": 10.0, "MoveDist": 0.5},"Wolf": {"MoveDist": 1.0},}'
        )
        return {
            "Sheep": {"InitPosLimit": 10.0, "MoveDist": 0.5},
            "Wolf": {"MoveDist": 1.0},
        }

    config = configparser.ConfigParser()
    if not config.read(filename):
        logging.critical(f"Configuration file does NOT exist.: {filename}")
        raise FileNotFoundError(f"Configuration file not found: {filename}")

    sheep_init_position_limit = config.getfloat("Sheep", "InitPosLimit")
    sheep_move_distance = config.getfloat("Sheep", "MoveDist")
    wolf_move_distance = config.getfloat("Wolf", "MoveDist")

    if (
        not 0 < sheep_init_position_limit < float("inf")
        or not 0 < sheep_move_distance < float("inf")
        or not 0 < wolf_move_distance < float("inf")
    ):
        logging.critical("Configuration values are NOT positive numbers")
        raise ValueError("All configuration values must be positive numbers.")
    logging.debug(
        f"Successfully received config data: config = { {'Sheep': {'InitPosLimit': sheep_init_position_limit, 'MoveDist': sheep_move_distance}, 'Wolf': {'MoveDist': wolf_move_distance}} }"
    )
    return {
        "Sheep": {
            "InitPosLimit": sheep_init_position_limit,
            "MoveDist": sheep_move_distance,
        },
        "Wolf": {
            "MoveDist": wolf_move_distance,
        },
    }
