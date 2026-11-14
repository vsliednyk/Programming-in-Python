import logging


def setup_logger(level):
    if level is None:
        logging.disable(logging.CRITICAL)
        return

    logging.basicConfig(
        filename="chase.log",
        filemode="w",
        level=level,
        format="%(levelname)s %(message)s",
    )