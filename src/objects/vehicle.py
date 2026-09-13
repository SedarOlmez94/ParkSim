"""
This module defines the Vehicle class and its associated properties and methods.
"""

import mesa
import numpy as np
import pandas as pd
import seaborn as sb


class Vehicle(mesa.Agent):
    def __init__(self, model, fuel_type: str, max_speed: float) -> None:
        super().__init__(model)

        self.fuel_type = fuel_type
        self.max_speed = max_speed
        # Initialize the position of the vehicle
        self.posx = 0
        self.posy = 0

    def get_fuel_type(self) -> str:
        return self.fuel_type

    def get_max_speed(self) -> float:
        return self.max_speed

    def get_position(self) -> tuple:
        return (self.posx, self.posy)

    def set_fuel_type(self, fuel_type: str) -> None:
        self.fuel_type = fuel_type

    def set_max_speed(self, max_speed: float) -> None:
        self.max_speed = max_speed

    def update_position(self, posx: float, posy: float) -> None:
        # Position will be based on the coordinate system of the environment either lat, lng or cartesian coordinates
        self.posx = posx
        self.posy = posy

    def accelerate(self) -> None:
        None


""" TIPS
self.model.agents -> a list of agents currently in the model. If you use random.choice(self.model.agents) a random active agent is selected.
"""
