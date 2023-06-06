"""
This module represents a Urban Garden.

Class:
    UrbanGarden: A class representing a Urban Garden. 
"""
from .garden import Garden


class UrbanGarden(Garden):
    """
    Class representing an Urban Garden.

    Attributes:
        area (float): The area of the garden.
        number_of_plant_containers (int): The number of plant containers in the garden.
        is_roof_top (bool): Indicates whether the garden is located on a rooftop.

    Methods:
        __init__(area=None, number_of_plant_containers=None, is_roof_top=None)
            Initializes an UrbanGarden instance.
        has_vegetable_garden()
            Checks if the garden has a vegetable garden.
        has_orchard()
            Checks if the garden has an orchard.
    """

    def __init__(
        self,
        area: float = None,
        number_of_plant_containers: int = None,
        is_roof_top: bool = None,
        plants: dict = (),
    ) -> None:
        """
        Initializes an UrbanGarden instance.

        Args:
            area (float, optional): The area of the garden.
            number_of_plant_containers (int, optional): The number of plant containers.
            is_roof_top (bool, optional): Indicates whether the garden is located on a rooftop.
        """
        self.number_of_plant_containers = number_of_plant_containers
        self.is_roof_top = is_roof_top
        super().__init__(area=area, flora_set={"vegetables", "flowers"}, plants=plants)

    def has_vegetable_garden(self) -> bool:
        """
        Checks if the garden has a vegetable garden.

        Returns:
            bool: True, indicating that it has a vegetable garden.
        """
        return True

    def has_orchard(self) -> bool:
        """
        Checks if the garden has an orchard.

        Returns:
            bool: False, indicating that it does not have an orchard.
        """
        return False
