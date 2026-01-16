def test_search_by_hub(fleet_manager_from_csv):
    assert len(fleet_manager_from_csv.search_by_hub("Downtown")) == 6
    assert len(fleet_manager_from_csv.search_by_hub("Airport")) == 6


def test_search_high_battery(fleet_manager_from_csv):
    vehicles = fleet_manager_from_csv.search_high_battery("Downtown")
    models = [v.model for v in vehicles]

    assert "Hyundai Ioniq 5" in models
    assert "Ather 450X" in models

def test_categorize_vehicles(fleet_manager_from_csv):
    categories = fleet_manager_from_csv.categorize_vehicles()

    assert "ElectricCar" in categories
    assert "ElectricScooter" in categories
    assert len(categories["ElectricCar"]) == 6
    assert len(categories["ElectricScooter"]) == 6
    
def test_sort_by_battery_level(fleet_manager_from_csv):
    fleet_manager_from_csv.sort_by_battery_level("Airport")

    batteries = [
        v.battery_percentage
        for v in fleet_manager_from_csv.fleet_hubs["Airport"]
    ]

    assert batteries == sorted(batteries, reverse=True)

def test_sort_by_model(fleet_manager_from_csv):
    sorted_vehicles = fleet_manager_from_csv.sort_by_model("Downtown")

    models = [v.model for v in sorted_vehicles]

    assert models == sorted(models)