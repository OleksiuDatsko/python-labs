# pylint: disable=line-too-long
"""
This module contains the `GardenSetManager` 

Classes:
    GardenSetManager: A class that manages a set of gardens and provides iteration and indexing functionality.
"""
from manager.garden_manager import GardenManager
from models.garden import Garden


class GardenSetManager:
    """
    A class that manages a set of gardens and provides iteration and indexing functionality.

    Args:
        garden_manager (GardenManager): An instance of GardenManager for managing the gardens.
    """

    def __init__(self, garden_manager: GardenManager = None) -> None:
        self.garden_manager = garden_manager
        self.garden = iter(garden_manager)
        self.flora = iter(garden_manager.gardens[0].plants.keys())
        self.garden_obj = next(self.garden)

    def __iter__(self):
        self.garden = iter(self.garden_manager)
        self.garden_obj = next(self.garden)
        self.flora = iter(self.garden_manager.gardens[0].plants.keys())
        return self

    def __next__(self):
        try:
            return next(self.flora)
        except StopIteration:
            self.garden_obj = next(self.garden)
            self.flora = iter(self.garden_obj.plants.keys())
            return next(self.flora)

    def __getitem__(self, key: int) -> Garden:
        garden_index = 0
        key -= len(self.garden_manager[garden_index].plants.keys())
        while key > 0:
            key -= len(self.garden_manager[garden_index].plants.keys())
            garden_index += 1
            if garden_index >= len(self.garden_manager):
                raise IndexError("garden manager out of range")
        return list(self.garden_manager[garden_index].plants.keys())[key]
