# pylint: disable=missing-module-docstring
from models.university_garden import UniversityGarden
from models.urban_garden import UrbanGarden
from models.farm_garden import FarmGarden
from models.botanic_garden import BotanicGarden
from manager.garden_manager import GardenManager
from manager.garden_set_manager import GardenSetManager

if __name__ == "__main__":
    gardens = [
        UniversityGarden(area=1.0, number_of_sculptures=100),
        UrbanGarden(area=2.0, number_of_plant_containers=10, is_roof_top=True),
        FarmGarden(area=3.0, number_of_tractors=10),
        BotanicGarden(area=4.0, number_of_greenhouses=10),
    ]
    garden_manager = GardenManager(gardens)
    garden_manager.add_garden(
        UrbanGarden(
            area=5.0,
            number_of_plant_containers=1,
            is_roof_top=True,
            plants={"vegetables": 10},
        )
    )
    garden_manager.add_garden(
        UrbanGarden(area=6.0, number_of_plant_containers=2, is_roof_top=True)
    )
    garden_manager.add_garden(
        UrbanGarden(area=7.0, number_of_plant_containers=3, is_roof_top=True)
    )
    garden_manager.add_gardens(gardens)
    garden_manager[0].plant("trees", 10)
    # garden_manager[0].remove("trees", 11)
    # garden_manager[0].remove("tree", 1)
    print("\n== has vegetable garden ==")
    for garden in garden_manager.find_all_with_vegetable_garden():
        print(garden)

    print("\n== has orchard ==")
    for garden in garden_manager.find_all_with_orchard():
        print(garden)

    print("\n== dict(bool) ==")
    for garden in garden_manager:
        print(garden.get_dict(bool))

    print("\n== enumerate ==")
    for index, garden in garden_manager.get_enumerate():
        print(index, garden)

    print("\n== zip ==")
    for has_orchard, garden in garden_manager.get_zip():
        print(f"has_orchard = {has_orchard}, {garden}")

    print("\n== all gardens ==")
    print(garden_manager)
    print("\n== have orchard ==")
    for key, value in garden_manager.have_orchard().items():
        print(f"{key} => {value}")
    print("\n== set manager ==")
    garden_set_manager = GardenSetManager(garden_manager)
    for garden_set in garden_set_manager:
        print(garden_set)
    print("\n== getitem[0] ==")
    print(garden_set_manager[0])
