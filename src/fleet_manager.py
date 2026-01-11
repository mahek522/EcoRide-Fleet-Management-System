from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class FleetManager:
    def __init__(self):
        
        self.fleet_hubs = {}  # {hub_name: [Vehicle objects]}

    def add_hub(self, hub_name):
        
        if hub_name not in self.fleet_hubs:
            self.fleet_hubs[hub_name] = []
            print(f"Hub '{hub_name}' added successfully.")
        else:
            print("Hub already exists.")

    def add_vehicle(self, hub_name, vehicle):
        
        if hub_name not in self.fleet_hubs:
            print("Hub does not exist.")
            return

        if vehicle in self.fleet_hubs[hub_name]:
            print("Duplicate Vehicle ID not allowed.")
        else:
            self.fleet_hubs[hub_name].append(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} added to {hub_name} hub.")

    def get_vehicles_by_hub(self, hub_name):
        
        return self.fleet_hubs.get(hub_name, [])
    
    def search_by_hub(self, hub_name):
        return self.fleet_hubs.get(hub_name, [])

    def search_high_battery(self, hub_name):
        return list(filter(
            lambda v: v.battery_percentage > 80,
            self.fleet_hubs.get(hub_name, [])
        ))
        
    vehicles = [
    ElectricCar("C101", "Tesla Model 3", 90, 5),
    ElectricScooter("S201", "Xiaomi Pro", 85, 25)
    ]
    
    for v in vehicles:
        print(f"{v.model} Trip Cost:", v.calculate_trip_cost(10))
    