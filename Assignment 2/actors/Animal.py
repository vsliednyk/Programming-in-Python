"""This is an abstract representation of actor role in our app"""
from typing import Tuple

class Animal:

    # Predefined parameters of class
    # __slots__ = ('pos_x', 'pos_y', 'step')
    def __init__(self, range : Tuple[float|int,float|int], step_size : float|int):
        self.pos_x , self.pos_y = range
        self.step = step_size
        pass

    def _get_x(self):
        return self.pos_x
    def _get_y(self):
        return self.pos_y
    def _get_step(self):
        return self.step


    def _set_x(self, new_val):
        self.pos_x = new_val
    def _set_y(self, new_val):
        self.pos_y = new_val

    def move(self,pos_x,pos_y):
        self._set_x(pos_x)
        self._set_y(pos_y)

    

