class Garden:
    """A class representing a garden.

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
        self.__area = area
        self.__has_orchard = has_orchard
        self.__has_vegetable_garden = has_vegetable_garden
        self.__number_of_flowers = number_of_flowers

    def plant_flower(self, count: int) -> None:
        """
        Adds a specified number of flowers to the garden.

        Args:
            count (int): The number of flowers to plant.
        """
        self.__number_of_flowers += count

    def remove_flower(self, count: int) -> None:
        """
        Removes a specified number of flowers from the garden.

        Args:
            count (int): The number of flowers to remove.
        """
        self.__number_of_flowers -= count if count > self.__number_of_flowers else 0

    def add_vegetable_region(self, area: float) -> None:
        """
        Adds an area to the garden.

        Args:
            area (float): The area to add to the garden.
        """
        self.__area += area

    def __str__(self) -> str:
        return f"area = {self.__area}, has_orchard = {self.__has_orchard}, has_vegetable_garden = {self.__has_vegetable_garden}, number_of_flowers = {self.__number_of_flowers}"

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, new_area):
        self.__area = new_area

    @property
    def has_orchard(self):
        return self.__has_orchard

    @has_orchard.setter
    def has_orchard(self, has_orchard):
        self.__has_orchard = has_orchard

    @property
    def has_vegetable_garden(self):
        return self.__has_vegetable_garden

    @has_vegetable_garden.setter
    def has_vegetable_garden(self, has_orchard):
        self.__has_vegetable_garden = has_orchard

    @property
    def number_of_flowers(self):
        return self.__number_of_flowers

    @number_of_flowers.setter
    def number_of_flowers(self, has_orchard):
        self.__number_of_flowers = has_orchard
