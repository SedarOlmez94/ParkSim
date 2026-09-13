'''
This module defines the Vehicle class and its associated properties and methods.
'''


class Vehicle:
    def __init__(self, id: int, fuel_type: str, max_speed: float) -> None:
        self.id = id
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def get_id(self) -> int:
        return self.id

    def get_fuel_type(self) -> str:
        return self.fuel_type

    def get_max_speed(self) -> float:
        return self.max_speed

    def set_id(self, id: int) -> None:
        self.id = id

    def set_fuel_type(self, fuel_type: str) -> None:
        self.fuel_type = fuel_type

    def set_max_speed(self, max_speed: float) -> None:
        self.max_speed = max_speed
