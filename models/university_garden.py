"""import abstract class"""
from .garden import Garden


class UniversityGarden(Garden):
    """
    Class representing a University Garden.

    Attributes:
        area (float): The area of the garden.
        number_of_sculptures (int): The number of sculptures in the garden.

    Methods:
        __init__(area=None, number_of_sculptures=None)
            Initializes a UniversityGarden instance.
        has_vegetable_garden()
            Checks if the garden has a vegetable garden.
        has_orchard()
            Checks if the garden has an orchard.
    """

    def __init__(self, area: float = None, number_of_sculptures: int = None) -> None:
        """
        Initializes a UniversityGarden instance.

        Args:
            area (float, optional): The area of the garden.
            number_of_sculptures (int, optional): The number of sculptures in the garden.
        """
        self.number_of_sculptures = number_of_sculptures
        super().__init__(area=area)

    def has_vegetable_garden(self) -> bool:
        """
        Checks if the garden has a vegetable garden.

        Returns:
            bool: False, indicating that it does not have a vegetable garden.
        """
        return False

    def has_orchard(self) -> bool:
        """
        Checks if the garden has an orchard.

        Returns:
            bool: False, indicating that it does not have an orchard.
        """
        return False

    def __str__(self, **kwargs) -> str:
        return super().__str__(class_name=self.__class__.__name__, **self.__dict__)
