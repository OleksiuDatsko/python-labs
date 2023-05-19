"""import abstract class"""
from models.garden import Garden


class GardenManager:
    """
    Class representing a Garden Manager.

    Attributes:
        gardens (list): A list of Garden objects.

    Methods:
        add_garden(garden)
            Adds a Garden object to the manager.
        add_gardens(gardens)
            Adds multiple Garden objects to the manager.
        find_all_with_vegetable_garden()
            Finds all gardens with a vegetable garden.
        find_all_with_orchard()
            Finds all gardens with an orchard.
    """

    def __init__(self, gardens: Garden = None) -> None:
        self.gardens = list(gardens) if gardens else []

    def add_garden(self, garden: Garden) -> None:
        """
        Adds a Garden object to the manager.

        Args:
            garden (Garden): The Garden object to add.
        """
        self.gardens.append(garden)

    def add_gardens(self, gardens) -> None:
        """
        Adds multiple Garden objects to the manager.

        Args:
            gardens (list): A list of Garden objects.
        """
        for garden in gardens:
            self.gardens.append(garden)

    def find_all_with_vegetable_garden(self) -> list:
        """
        Finds all gardens with a vegetable garden.

        Returns:
            list: A list of Garden objects with a vegetable garden.
        """
        return [garden for garden in self.gardens if garden.has_vegetable_garden()]
        # return list(filter(lambda garden: garden.has_vegetable_garden(), self.gardens))

    def find_all_with_orchard(self) -> list:
        """
        Finds all gardens with an orchard.

        Returns:
            list: A list of Garden objects with an orchard.
        """
        # return [garden for garden in self.gardens if garden.has_orchard()]
        return list(filter(lambda garden: garden.has_orchard(), self.gardens))

    def __str__(self):
        result = "Garden manager:\n"
        result += "\n".join([str(garden) for garden in self.gardens])
        return result
