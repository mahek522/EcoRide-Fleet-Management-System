from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = 0
        self.__maintenance_status = "Available"
        self.__rental_price = None 

        self.set_battery_percentage(battery_percentage)

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, status):
        self.__maintenance_status = status
        
    def get_rental_price(self):
        return self.__rental_price
    
    def set_rental_price(self, rental_price):
        if rental_price < 0:
            print("Rental Price should be positive")
        self.__rental_price = rental_price
    
    def get_battery_percentage(self):
        return self.__battery_percentage

    def set_battery_percentage(self, value):
        if 0 <= value <= 100:
            self.battery_percentage = value
        else:
            raise ValueError("Battery must be between 0 and 100")
        
    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass
    
    def __eq__(self, other):
        return self.vehicle_id == other.vehicle_id
    
    def __str__(self):
        return f"{self.vehicle_id} | {self.model} | Battery level: {self.battery_percentage}% | Status: {self.get_maintenance_status()}"
