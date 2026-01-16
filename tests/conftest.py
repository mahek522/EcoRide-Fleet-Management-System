import pytest
import csv

from src.fleet_manager import FleetManager
from src.electric_car import ElectricCar
from src.electric_scooter import ElectricScooter


@pytest.fixture
def fleet_manager_from_csv():
    fm = FleetManager()

    with open("fleet_data.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            hub = row["Fleet-Hub"]

            if row["Type"] == "ElectricCar":
                vehicle = ElectricCar(
                    row["Vehicle ID"],
                    row["Model"],
                    int(row["Battery"])
                )
            else:
                vehicle = ElectricScooter(
                    row["Vehicle ID"],
                    row["Model"],
                    int(row["Battery"])
                )

            fm.add_hub(hub)
            fm.add_vehicle(hub, vehicle)

    return fm
