"""import abstract class"""
from .garden import Garden


class BotanicGarden(Garden):
    """
    Class representing a Botanic Garden.

    Attributes:
        area (float): The area of the garden.
        number_of_greenhouses (int): The number of greenhouses in the garden.

    Methods:
        has_vegetable_garden()
            Checks if the garden has a vegetable garden.
        has_orchard()
            Checks if the garden has an orchard.
    """

    def __init__(self, area: float = None, number_of_greenhouses: int = None) -> None:
        """
        Initializes a BotanicGarden instance.

        Args:
            area (float, optional): The area of the garden.
            number_of_greenhouses (int, optional): The number of greenhouses in the garden.
        """
        self.number_of_greenhouses = number_of_greenhouses
        super().__init__(area=area)

    def has_vegetable_garden(self) -> bool:
        """
        Checks if the garden has a vegetable garden.

        Returns:
            bool: False, it has no vegetable garden.
        """
        return False

    def has_orchard(self) -> bool:
        """
        Checks if the garden has an orchard.

        Returns:
            bool: True, it has an orchard.
        """
        return True

    def __str__(self, **kwargs) -> str:
        return super().__str__(class_name=self.__class__.__name__, **self.__dict__)
