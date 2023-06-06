"""
This module provides an abstract class representing a garden.

Classes:
    Garden (ABC): An abstract class representing a garden.
"""
from abc import ABC, abstractmethod
from tools.decorators import logged

from tools.exceptions import NoPlantInTheGardenException, NotEnoughPlantsException


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
        self, area: float = None, flora_set: set = (), plants: dict = ()
    ) -> None:
        self.area = area
        self.plants = (
            dict.fromkeys(flora_set, 0)
            if plants == ()
            else {key: plants.get(key, 0) for key in flora_set}
        )

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

    @logged(NoPlantInTheGardenException, mode="file")
    def plant(self, plant_type: str, number_of_plants: int) -> None:
        """
        Plant a specified number of plants of the given type in the garden.

        Args:
            plant_type (str): The type of plant to be planted.
            number_of_plants (int): The number of plants to be planted.

        Raises:
            NoPlantInTheGardenException: If the specified plant type is not available in the garden.

        Returns:
            None
        """
        if plant_type not in self.plants.keys():
            raise NoPlantInTheGardenException("There is no place to plant this plant.")
        self.plants[plant_type] += number_of_plants

    @logged(NotEnoughPlantsException, mode="file")
    def remove(self, plant_type: str, number_of_plants: int) -> None:
        """
        Remove a specified number of plants of the given type from the garden.

        Args:
            plant_type (str): The type of plant to be removed.
            number_of_plants (int): The number of plants to be removed.

        Raises:
            NoPlantInTheGardenException: If the specified plant type is not available in the garden.
            NotEnoughPlantsException: If there are not enough plants of the specified type in the garden.

        Returns:
            None
        """
        if plant_type not in self.plants.keys():
            raise NoPlantInTheGardenException(
                "The specified plant does not exist in the garden."
            )
        if self.plants[plant_type] < number_of_plants:
            raise NotEnoughPlantsException(
                "Not enough plants of the specified type in the garden."
            )
        self.plants[plant_type] -= number_of_plants

    def __str__(self) -> str:
        result = f"{self.__class__.__name__}: "
        for attributes, values in self.__dict__.items():
            result += f"{attributes} = {values}; "
        return result

    def __iter__(self) -> set:
        return iter(self.plants.keys())
