"""Main loop of our simulation"""

from typing import Dict, Tuple, TypeAlias, TypedDict
from Wolf import Wolf
from Sheep import Sheep
""" Expects:
    - config:{
        "Sheep":{
            "InitPosLimit"  :   float,
            "MoveDist"      :   float
            },
        "Wolf":{
            "MoveDist" : float
                }
            }"""


SheepConfigType: TypeAlias = Dict[str, float]
WolfConfigType: TypeAlias = Dict[str, float]
ConfigType: TypeAlias = Dict[str, SheepConfigType | WolfConfigType]


def simulate():
    config = {
        "Sheep":{
            "InitPosLimit": 10.0,
            "MoveDist": 1.0
        },
        "Wolf":{
            "MoveDist": 0.75
        }
    }
    amount_of_sheep = 10
    max_rounds = 50
    preset = []
    alive_sheep = []
    #params
    
    
    amount_alive = amount_of_sheep
    list_of_sheep = []
    
    if preset:
        list_of_sheep = preset
        alive_sheep = [sheep for sheep in list_of_sheep if sheep.is_alive()]
        amount_alive = len(alive_sheep)
    else:
        list_of_sheep = [Sheep(i,config["Sheep"]["InitPosLimit"],config["Sheep"]["MoveDist"] ) for i in range(amount_of_sheep)]
    
    wolf = Wolf((0,0), config["Wolf"]["MoveDist"])
    round_index = 1
    
    while round_index <= max_rounds and amount_alive > 0:

        alive_sheep = [sheep for sheep in list_of_sheep if sheep.is_alive()]
        

        for sheep in alive_sheep:
            sheep.move_randomly()
        

        result = wolf.try_catching(list_of_sheep=alive_sheep)
        
        if result["result"] == 'eaten':
            amount_alive -= 1
            

        round_index += 1

    print("Amount of sheep left:", amount_alive)
    

    alive_sheep = [sheep for sheep in list_of_sheep if sheep.is_alive()]
    print([(sheep.pos_x, sheep.pos_y) for sheep in alive_sheep])
    return 0


if __name__ == "__main__":
    simulate()
    print()
