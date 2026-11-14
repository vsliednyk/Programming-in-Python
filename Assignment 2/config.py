import argparse


def positive_int(number):
    number = int(number)
    if number > 0:
        return number
    raise argparse.ArgumentTypeError(f"{number} is not a positive integer")


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Wolf-Sheep simulation',
        description='Simulation involving a wolf that tries '
                    'to catch sheep scattered in a meadow',
    )
    parser.add_argument(
        '-c', '--config',
        type=str,
        help='configuration file'
    )

    log_choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    parser.add_argument(
        '-l', '--log',
        type=str,
        choices=log_choices,
        help='set the logging level'
    )

    parser.add_argument(
        '-r', '--rounds',
        type=positive_int,
        default=50,
        help='number of rounds'
    )

    parser.add_argument(
        '-s', '--sheep',
        type=positive_int,
        default=15,
        help='sheep amount'
    )

    parser.add_argument(
        '-w', '--wait',
        action='store_true',
        help='wait for input between rounds'
    )

    return parser.parse_args()