from typing import Tuple
from Animal import Animal
class Sheep(Animal):

    def __init__(self, range : Tuple[float|int,float|int], step_size : float|int):
        super().__init__(range=range, step_size=step_size)