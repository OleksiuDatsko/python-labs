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

    def __str__(self) -> str:
        result = f"{self.__class__.__name__}: "
        for attributes, values in self.__dict__.items():
            result += f"{attributes} = {values}; "
        return result