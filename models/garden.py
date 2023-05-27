"""
This module provides an abstract class representing a garden.

Classes:
    Garden (ABC): An abstract class representing a garden.
"""
from abc import ABC, abstractmethod


class Garden(ABC):
    """
    An abstract class representing a garden.

    Attributes:
        area (float): The area of the garden.

    Methods:
        plant_flower(self, count)
            Adds a specified number of flowers to the garden.
        remove_flower(self, count)
            Removes a specified number of flowers from the garden.
        add_vegetable_region(self, area)
            Adds an area to the garden.

    Properties:
        area
            The area of the garden in hectars.
    """

    def __init__(self, area: float = None, flora_set: set = ()) -> None:
        self.area = area
        self.flora_set = flora_set

    @abstractmethod
    def has_vegetable_garden(self) -> bool:
        """
        Check is garden have vegetable garden

        Returns:
            bool: if garden has vegeable garden
        """

    @abstractmethod
    def has_orchard(self) -> bool:
        """
        Check if garden has orchard

        Returns:
            bool: if garden has orchard
        """

    # pylint: disable=line-too-long
    def get_dict(self, data_type: type) -> dict:
        """
        Returns a dictionary containing the keys and values of object's attributes, filtered by a specific data type.

        Args:
            data_type: The data type used to filter the attributes.
            Only attributes with values of this data type will be included in the dictionary.

        Returns:
            dict: A dictionary with the filtered attribute keys and values.
        """
        return {
            key: value
            for (key, value) in self.__dict__.items()
            if isinstance(value, data_type)
        }

    def __str__(self) -> str:
        result = f"{self.__class__.__name__}: "
        for attributes, values in self.__dict__.items():
            result += f"{attributes} = {values}; "
        return result

    def __iter__(self) -> set:
        return iter(self.flora_set)
