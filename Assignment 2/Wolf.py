from typing import Tuple
from math import sqrt
from Animal import Animal
from Sheep import Sheep

class Wolf(Animal):

    """The function expect list of alive sheep"""
    # Returns index of sheep being caught or signalizing just movement
    def try_catching(self, list_of_sheep: list[Sheep]):

        if not list_of_sheep:
            return {"result":"ERROR: No sheep parsed",
                  "sheep_id": -404}
        
        wolf_x, wolf_y = self.pos_x, self.pos_y

        min_dist_squared = float('inf')
        index_of_closest_sheep = -1
        min_diff_x = 0
        min_diff_y = 0

        # Calculating distances
        for i, sheep in enumerate(list_of_sheep):
            diff_x = sheep.pos_x - wolf_x
            diff_y = sheep.pos_y - wolf_y
            distance_squared = diff_x * diff_x + diff_y * diff_y
            # Determining the closest one
            if distance_squared<min_dist_squared:
                min_diff_x = diff_x
                min_diff_y = diff_y
                min_dist_squared = distance_squared
                index_of_closest_sheep = i

        sheep_to_catch = list_of_sheep[index_of_closest_sheep]
        closest_sheep_id = sheep_to_catch.get_id()
        sheep_x, sheep_y = sheep_to_catch.pos_x, sheep_to_catch.pos_y
        # Catching a sheep
        if min_dist_squared <= self.step*self.step:
            self.move(sheep_x, sheep_y)
            sheep_to_catch.set_killed()
            return {"result":"eaten",
                  "sheep_id": closest_sheep_id}
        # Moving towards the closest sheep
        self.move_towards(
            min_diff_x, 
            min_diff_y,
            sqrt(min_dist_squared)
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