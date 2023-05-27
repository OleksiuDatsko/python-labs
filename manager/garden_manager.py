"""import abstract class"""
from typing import Iterable

from models.garden import Garden
from tools.decorators import limit_calls, number_of_arguments_in_method


class GardenManager:
    """
    Class representing a Garden Manager.

    Attributes:
        gardens (list): A list of Garden objects.

    Methods:
        add_garden(garden)
            Adds a Garden object to the manager.
        add_gardens(gardens)
            Adds multiple Garden objects to the manager.
        find_all_with_vegetable_garden()
            Finds all gardens with a vegetable garden.
        find_all_with_orchard()
            Finds all gardens with an orchard.
    """

    def __init__(self, gardens: Iterable = ()) -> None:
        self.gardens = list(gardens)

    @limit_calls(3)
    def add_garden(self, garden: Garden) -> None:
        """
        Adds a Garden object to the manager.

        Args:
            garden (Garden): The Garden object to add.
        """
        self.gardens.append(garden)

    @number_of_arguments_in_method
    def add_gardens(self, gardens: list[Garden]) -> None:
        """
        Adds multiple Garden objects to the manager.

        Args:
            gardens (list): A list of Garden objects.
        """
        self.gardens += gardens

    def find_all_with_vegetable_garden(self) -> list:
        """
        Finds all gardens with a vegetable garden.

        Returns:
            list: A list of Garden objects with a vegetable garden.
        """
        return [garden for garden in self.gardens if garden.has_vegetable_garden()]

    def find_all_with_orchard(self) -> list:
        """
        Finds all gardens with an orchard.

        Returns:
            list: A list of Garden objects with an orchard.
        """
        return [garden for garden in self.gardens if garden.has_orchard()]

    def get_lsit_of_has_orchard(self) -> list[bool]:
        """
        Returns a list of boolean values indicating whether each garden in manager has an orchard.

        Returns:
            list[bool]: A list of boolean values.
                        indicating whether the garden has an orchard (True) or not (False).
        """
        return [garden.has_orchard() for garden in self.gardens]

    def get_enumerate(self):
        """
        Get the enumerated list of gardens.

        Returns:
            list: A list of tuples containing the index and garden object.
        """
        return list(enumerate(self.gardens))

    def get_zip(self):
        """
        Get a zipped list of orchard status and gardens.

        Returns:
            list: A list of tuples containing the orchard status and corresponding garden object.
        """
        return list(zip(self.get_lsit_of_has_orchard(), self.gardens))

    def is_all_have_orchard(self) -> bool:
        """
        Check if all gardens have an orchard.

        Returns:
            bool: True if all gardens have an orchard, False otherwise.
        """
        return all(self.get_lsit_of_has_orchard())

    def is_at_least_one_have_orchard(self) -> bool:
        """
        Check if at least one garden has an orchard.

        Returns:
            bool: True if at least one garden has an orchard, False otherwise.
        """
        return any(self.get_lsit_of_has_orchard())

    def __str__(self) -> str:
        result = "Garden manager:\n"
        result += "\n".join([str(garden) for garden in self.gardens])
        return result

    def __len__(self) -> int:
        return len(self.gardens)

    def __getitem__(self, garden_number: int) -> Garden:
        return self.gardens[garden_number]

    def __iter__(self):
        return iter(self.gardens)
