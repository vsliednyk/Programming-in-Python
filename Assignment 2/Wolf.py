from typing import Tuple
from math import sqrt
from Animal import Animal
from Sheep import Sheep

class Wolf(Animal):

    def __init__(self, position : Tuple[float|int,float|int], step_size : float|int):
        super().__init__(position=position, step_size=step_size)

    """The function expect list of alive sheep"""
    # Returns index of sheep being caught or signalizing just movement
    def try_catching(self, list_of_sheep: list[Sheep]):

        if not list_of_sheep:
            return {"result":"ERROR: No sheep parsed",
                  "sheep_id": -404}
        # Calculating distances
        
        diffs_x = [sheep.pos_x - self.pos_x for sheep in list_of_sheep]
        diffs_y = [sheep.pos_y - self.pos_y for sheep in list_of_sheep]
        distances = [diff_x * diff_x + diff_y * diff_y for diff_x,diff_y in zip(diffs_x,diffs_y)]
        # Determining the smallest one
        min_distance = min(distances)
        index_of_closest_sheep = distances.index(min_distance)
        sheep_to_catch = list_of_sheep[index_of_closest_sheep]
        closest_sheep_id = sheep_to_catch.get_id()
        sheep_x, sheep_y = sheep_to_catch.pos_x, sheep_to_catch.pos_y
        # Catching a sheep
        if min_distance <= self.step*self.step:
            self.move(sheep_x, sheep_y)
            sheep_to_catch.set_killed()
            return {"result":"eaten",
                  "sheep_id": closest_sheep_id}
        # Moving towards the closest sheep
        self.move_towards(
            diffs_x[index_of_closest_sheep], 
            diffs_y[index_of_closest_sheep],
            sqrt(min_distance)
            )
        return {"result":"chasing",
                  "sheep_id": closest_sheep_id}

    # Moves towards closest sheep
    def move_towards(self, diff_x, diff_y, distance):
        vec_x = diff_x / distance
        vec_y = diff_y / distance
        self.move( pos_x=(self.pos_x + vec_x * self.step),
                   pos_y=(self.pos_y + vec_y * self.step)
                   )