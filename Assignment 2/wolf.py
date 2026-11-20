from math import sqrt
from animal import Animal
from sheep import Sheep

import logging

class Wolf(Animal):
    def find_closest_sheep(self, list_of_sheep: list[Sheep]):
        logging.debug("Entering finding closest shep function")
        wolf_x, wolf_y = self.pos_x, self.pos_y
        closest_index: int | None = None
        min_dist_squared = float("inf")
        min_diff_x = 0
        min_diff_y = 0

        for i, sheep in enumerate(list_of_sheep):
            diff_x = sheep.pos_x - wolf_x
            diff_y = sheep.pos_y - wolf_y
            distance_squared = diff_x * diff_x + diff_y * diff_y

            if distance_squared < min_dist_squared:
                min_diff_x = diff_x
                min_diff_y = diff_y
                min_dist_squared = distance_squared
                closest_index = i
                
        return closest_index, min_dist_squared, min_diff_x, min_diff_y

    def catch_action(self, sheep: Sheep):
        logging.info("Wolf moved")
        self.move(sheep.pos_x, sheep.pos_y)
        logging.debug(
            "New wolf position is: (%s, %s)",
            self.pos_x,
            self.pos_y,
        )
        sheep.set_killed()

    def catch_attempt(self, min_dist_squared, min_diff_x, min_diff_y, sheep):
        logging.debug("Attempting to catch a sheep")
        closest_sheep_id = sheep.get_id()
        if min_dist_squared <= self.step * self.step:
            self.catch_action(sheep=sheep)
            logging.info("Sheep got caught! sheep_id: %s", closest_sheep_id)
            return {"result": "eaten", "sheep_id": closest_sheep_id}
        logging.debug(
            "Moving towards the closest sheep. sheep_id: %s",
            closest_sheep_id,
        )
        self.move_towards(min_diff_x, min_diff_y, sqrt(min_dist_squared))
        return {"result": "chasing", "sheep_id": closest_sheep_id}

    def try_catching(self, list_of_sheep: list[Sheep]):
        if not list_of_sheep:
            logging.critical("No sheep parsed")
            return {"result": "ERROR: No sheep parsed", "sheep_id": -404}

        closest_index, min_dist_squared, min_diff_x, min_diff_y = (
            self.find_closest_sheep(list_of_sheep=list_of_sheep)
        )

        if closest_index is None:
            return {
                "result": "ERROR: Didn't find closest sheep index",
                "sheep_id": None,
            }
        
        sheep_to_catch = list_of_sheep[closest_index]
        logging.debug(
            "Wolf determined closest sheep: %s at distance %s",
            sheep_to_catch.sheep_id,
            sqrt(min_dist_squared),
        )
        
        return self.catch_attempt(
            min_dist_squared=min_dist_squared,
            min_diff_x=min_diff_x,
            min_diff_y=min_diff_y,
            sheep=sheep_to_catch,
        )

    def move_towards(self, diff_x, diff_y, distance):
        
        vec_x = diff_x / distance
        vec_y = diff_y / distance
        self.move(
            pos_x=(self.pos_x + vec_x * self.step),
            pos_y=(self.pos_y + vec_y * self.step),
        )