import random

from Animal import Animal


class Sheep(Animal):
    DIRECTIONS = ("north", "south", "east", "west")

    def __init__(self, id: int, init_position_limit: float, step_size: float):
        self.alive = True
        self.id = id
        position_x = random.uniform(-init_position_limit, init_position_limit)
        position_y = random.uniform(-init_position_limit, init_position_limit)
        super().__init__(position=(position_x, position_y), step_size=step_size)

    def move_randomly(self):
        direction = random.choice(self.DIRECTIONS)

        new_position_x = self.pos_x
        new_position_y = self.pos_y

        if direction == "north":
            new_position_y += self.step
        elif direction == "south":
            new_position_y -= self.step
        elif direction == "east":
            new_position_x += self.step
        elif direction == "west":
            new_position_x -= self.step

        self.move(new_position_x, new_position_y)

        return direction

    def get_id(self):
        return self.id

    def is_alive(self):
        return self.alive

    def set_killed(self):
        self.alive = False
        
