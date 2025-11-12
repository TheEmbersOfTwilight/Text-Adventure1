import json
from dataclasses import dataclass, asdict

@dataclass
class GameState:
    arins_rise=False #Whether the player has helped Arin rise to power
    razor=0 #How many razors the player has
    wand=False #Whether the player has picked up the wand
    door1=False #Whether the player has opened the door
    potion1=False #Whether the player has taken the potion beaker
    timewasted=False #Whether the player wasted time trying to pick the flowers by hand
    scars=False #Whether the player has scars
    flowers_collected=False #Whether the player has collected the moonshade flowers
    water_collected=False #Whether the player has collected the water from the river
    infinite_razor_counter=0 #Once it hits 20, it will start giving the player infinite razors
    powerupgraded=0 #How much the player's power has been upgraded
    callout_counter=0 #How many times the player has called out through the bars
    day_night_cycle=0 #0 = Day, 1 = Night

    def save(self, filepath: str):
        with open(filepath, "w") as file:
            json.dump(asdict(self), file, indent=4)

    @classmethod
    def load(cls, filepath: str):
        with open(filepath, "r") as file:
            data = json.load(file)
        return cls(**data)
