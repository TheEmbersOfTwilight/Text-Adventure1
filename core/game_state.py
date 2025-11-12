import json
from dataclasses import dataclass, asdict, field

@dataclass
class GameState:
    arins_rise: bool = field(default=False) #Whether the player has helped Arin rise to power
    razor: int = field(default=0) #How many razors the player has
    wand: bool = field(default=False) #Whether the player has picked up the wand
    door1: bool = field(default=False) #Whether the player has opened the door
    potion1: bool = field(default=False) #Whether the player has taken the potion beaker
    timewasted: bool = field(default=False) #Whether the player wasted time trying to pick the flowers by hand
    scars: bool = field(default=False) #Whether the player has scars
    flowers_collected: bool = field(default=False) #Whether the player has collected the moonshade flowers
    water_collected: bool = field(default=False) #Whether the player has collected the water from the river
    infinite_razor_counter: int = field(default=0) #Once it hits 20, it will start giving the player infinite razors
    powerupgraded: int = field(default=0) #How much the player's power has been upgraded
    callout_counter: int = field(default=0) #How many times the player has called out through the bars
    day_night_cycle: int = field(default=0) #0 = Day, 1 = Night

    def save(self, filepath: str):
        with open(filepath, "w") as file:
            json.dump(asdict(self), file, indent=4)

    @classmethod
    def load(cls, filepath: str):
        with open(filepath, "r") as file:
            data = json.load(file)
        return cls(**data)
