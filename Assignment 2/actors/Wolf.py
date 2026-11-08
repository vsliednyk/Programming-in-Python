from typing import Tuple
from Animal import Animal

class Wolf(Animal):

    def __init__(self, self, range : Tuple[float|int,float|int], step_size : float|int):
        super().__init__(range=range, step_size=step_size)

    def move_towards(self,des_x,des_y):

        pass