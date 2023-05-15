"""This module defines a Garden class representing a garden"""


class Garden:
    """
    A class representing a garden.

    Attributes:
        __area (float): The area of the garden.
        __has_orchard (bool): Indicates whether the garden has an orchard.
        __has_vegetable_garden (bool): Indicates whether the garden has a vegetable garden.
        __number_of_flowers (int): The number of flowers in the garden.

    Methods:
        plant_flower(self, count)
            Adds a specified number of flowers to the garden.
        remove_flower(self, count)
            Removes a specified number of flowers from the garden.
        add_vegetable_region(self, area)
            Adds an area to the garden.
        __str__(self)
            Returns a string representation of the Garden object.

    Properties:
        area
            The area of the garden.
        has_orchard
            Indicates whether the garden has an orchard.
        has_vegetable_garden
            Indicates whether the garden has a vegetable garden.
        number_of_flowers
            The number of flowers in the garden.
    """

    def __init__(
        self,
        area: float = None,
        has_orchard: bool = None,
        has_vegetable_garden: bool = None,
        number_of_flowers: int = None,
    ) -> None:
        self.area = area
        self.has_orchard = has_orchard
        self.has_vegetable_garden = has_vegetable_garden
        self.number_of_flowers = number_of_flowers

    garden_instance = None

    def plant_flower(self, count: int) -> None:
        """
        Adds a specified number of flowers to the garden.

        Args:
            count (int): The number of flowers to plant.
        """
        self.number_of_flowers += count

    def remove_flower(self, count: int) -> None:
        """
        Removes a specified number of flowers from the garden.

        Args:
            count (int): The number of flowers to remove.
        """
        self.number_of_flowers -= count if count > self.number_of_flowers else 0

    def add_vegetable_region(self, area: float) -> None:
        """
        Adds an area to the garden.

        Args:
            area (float): The area to add to the garden.
        """
        self.area += area

    def __str__(self):
        return (
            f"Gardeb(area = {self.area}, "
            f"has_orchard = {self.has_orchard}, "
            f"has_vegetable_garden = {self.has_vegetable_garden}, "
            f"number_of_flowers = {self.number_of_flowers})"
        )

    @staticmethod
    def get_instance() -> "Garden":
        """
        Return the default instance of the Garden singleton class.

        Args:
            **kwargs: Arbitrary keyword arguments to initialize the Garden object.

        Returns:
            Garden: The instance of the Garden singleton class.

        """
        if Garden.garden_instance is None:
            Garden.garden_instance = Garden()
        return Garden.garden_instance
