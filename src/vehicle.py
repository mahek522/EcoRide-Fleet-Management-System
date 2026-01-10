from abc import ABC, abstractmethod

print("Welcome to Eco-Ride Urban Mobility System")

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__maintenance_status = "Available"
        self.set_battery_percentage(battery_percentage)

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def set_battery_percentage(self, value):
        if 0 <= value <= 100:
            self.battery_percentage = value
        else:
            raise ValueError("Battery must be between 0 and 100")
    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass