"""Abstract Base Classes (ABC) module"""
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

    @abstractmethod
    def __init__(
        self,
        area: float = None,
    ) -> None:
        self.area = area

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

    @abstractmethod
    def __str__(self, **kwargs) -> str:
        result = f"{kwargs.pop('class_name', 'Garden')}: "
        for attributes, values in kwargs.items():
            result += f"{attributes} = {values}; "
        return result
