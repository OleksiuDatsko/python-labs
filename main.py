from garden import Garden

if __name__ == "__main__":
    gardens = [
        Garden(
            area=10.0,
            has_orchard=True,
            has_vegetable_garden=False,
            number_of_flowers=100,
        ),
        Garden(),
        Garden.get_instance(),
        Garden.get_instance(),
    ]
    res = gardens[1:3]
    print(res)
    print("\n".join(str(garden) for garden in gardens))
