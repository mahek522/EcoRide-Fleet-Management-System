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
        
    def categorize_vehicles(self):
        categories = {}
        for vehicles in self.fleet_hubs.values():
            for v in vehicles:
                vehicle_type = type(v).__name__
                if vehicle_type not in categories:
                    categories[vehicle_type] = []
                categories[vehicle_type].append(v)
        return categories

    def display_categorized_vehicles(self):
        categorized_vehicles = self.categorize_vehicles()
        for vehicle_type, vehicles in categorized_vehicles.items():
            print(f"--- {vehicle_type}s ---")
            for vehicle in vehicles:
                print(f"ID: {vehicle.vehicle_id}, Model: {vehicle.model}, Battery: {vehicle.battery_percentage}%")
            print()  # Blank line for better readability
            
if __name__ == "__main__":
    fleet_manager = FleetManager()
    # Example usage
    fleet_manager.add_hub("Downtown")
    fleet_manager.add_vehicle("Downtown", ElectricCar("C101", "Tesla Model 3", 90, 5))
    fleet_manager.add_vehicle("Downtown", ElectricScooter("S201", "Xiaomi Pro", 85, 25))
    
    # Display categorized vehicles
    fleet_manager.display_categorized_vehicles()