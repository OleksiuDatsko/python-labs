"""import all models"""
from models.university_garden import UniversityGarden
from models.urban_garden import UrbanGarden
from models.farm_garden import FarmGarden
from models.botanic_garden import BotanicGarden
from manager.garden_manager import GardenManager

if __name__ == "__main__":
    gardens = [
        UniversityGarden(area=1, number_of_sculptures=100),
        UrbanGarden(area=2, number_of_plant_containers=10, is_roof_top=True),
        FarmGarden(area=3, number_of_tractors=10),
        BotanicGarden(area=4, number_of_greenhouses=10),
    ]
    garden_manager = GardenManager(gardens=gardens)
    print("== has vegetable garden ==")
    for garden in garden_manager.find_all_with_vegetable_garden():
        print(str(garden))
    print("== has orchard ==")
    for garden in garden_manager.find_all_with_orchard():
        print(str(garden))
    print("== all gardens ==")
    print(garden_manager)
