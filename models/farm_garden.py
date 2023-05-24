"""import abstract class"""
from .garden import Garden


class FarmGarden(Garden):
    """
    Class representing a Farm Garden.

    Attributes:
        area (float): The area of the garden.
        number_of_tractors (int): The number of tractors in the garden.

    Methods:
        has_vegetable_garden()
            Checks if the garden has a vegetable garden.
        has_orchard()
            Checks if the garden has an orchard.
    """

    def __init__(self, area: float = None, number_of_tractors: int = None) -> None:
        """
        Initializes a FarmGarden instance.

        Args:
            area (float, optional): The area of the garden.
            number_of_tractors (int, optional): The number of tractors in the garden.
        """
        self.number_of_tractors = number_of_tractors
        super().__init__(area)

    def has_vegetable_garden(self) -> bool:
        """
        Checks if the garden has a vegetable garden.

        Returns:
            bool: True, since it has a vegetable garden.
        """
        return True

    def has_orchard(self) -> bool:
        """
        Checks if the garden has an orchard.

        Returns:
            bool: True, since it has an orchard.
        """
        return True
