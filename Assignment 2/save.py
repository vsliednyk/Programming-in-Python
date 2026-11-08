import csv
import json


def save_positions(position_history):
    """Save round positions to JSON.

    Example:
        position_history = [
            {
                "round_no": 1,
                "wolf_pos": (0.0, 1.0),
                "sheep_pos": [(6.7, 3.0), None, (-1.6, 7.0)]
            }
        ]
    """
    with open("pos.json", "w", encoding="utf-8") as file:
        json.dump(position_history, file, indent=4)


def save_alive(alive_history):
    """Save alive sheep counts to CSV.

    Example:
        alive_history = [
            (1, 3),
            (2, 2),
            (3, 2)
        ]
    """
    with open("alive.csv", "w", encoding="utf-8", newline="") as file:
        csv_writer = csv.writer(file)
        for alive in alive_history:
            csv_writer.writerow(alive)