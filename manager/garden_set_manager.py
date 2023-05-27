"""import regular garden manager"""
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
        self.garden_index = 0
        self.flora_set_index = 0

    def __iter__(self):
        self.garden_index = 0
        self.flora_set_index = 0
        return self

    def __next__(self):
        if self.flora_set_index < len(self.garden_manager[self.garden_index].flora_set):
            item = list(self.garden_manager[self.garden_index].flora_set)[
                self.flora_set_index
            ]
            self.flora_set_index += 1
            return item
        self.garden_index += 1
        if self.garden_index >= len(self.garden_manager):
            raise StopIteration
        self.flora_set_index = 0
        item = list(self.garden_manager[self.garden_index].flora_set)[
            self.flora_set_index
        ]
        self.flora_set_index += 1
        return item

    def __getitem__(self, key: int) -> Garden:
        garden_index = 0
        key -= len(self.garden_manager[garden_index].flora_set)
        while key > 0:
            key -= len(self.garden_manager[garden_index].flora_set)
            garden_index += 1
            if garden_index >= len(self.garden_manager):
                raise IndexError("garden manager out of range")
        return list(self.garden_manager[garden_index].flora_set)[key]
