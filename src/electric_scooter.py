from src.vehicle import Vehicle


class ElectricScooter(Vehicle):
    
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit=60):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit
    
    def calculate_trip_cost(self, minutes):
        return 1 + (0.15 * minutes)