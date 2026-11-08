"""This is an abstract representation of actor role in our app"""
from typing import Tuple

class Animal:

    # Predefined parameters of class
    # __slots__ = ('pos_x', 'pos_y', 'step')
    def __init__(self, position : Tuple[float|int,float|int], step_size : float|int):
        self.pos_x, self.pos_y = position
        self.step = step_size

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y