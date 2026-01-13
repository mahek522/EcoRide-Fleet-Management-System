from fleet_manager import FleetManager
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


def display_menu():
    print("\n-------- Eco-Ride Urban Mobility System --------")
    print("1. Add Hub")
    print("2. Add Vehicle to Hub")
    print("3. View Vehicles in Hub")
    print("4. Search Vehicles by Hub")
    print("5. Search High Battery Vehicles (>80%)")
    print("6. Categorized View (Car / Scooter)")
    print("7. Fleet Analytics")
    print("8. Sort Vehicles by Model")
    print("9. Sort Vehicles by Battery (High → Low)")
    print("10. Add Data to CSV")
    print("11. Add Data to JSON")
    print("12. Exit")


def main():
    print("Welcome to Eco-Ride Urban Mobility System 🚗🛴")
    manager = FleetManager()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-12): ")

        # 1. Add Hub(UC6)
        if choice == "1":
            hub_name = input("Enter hub name: ")
            manager.add_hub(hub_name)

        # 2. Add Vehicle(UC6)
        elif choice == "2":
            hub_name = input("Enter hub name: ")

            print("Select Vehicle Type")
            print("1. Electric Car")
            print("2. Electric Scooter")
            vehicle_type = input("Enter choice: ")

            vehicle_id = input("Enter Vehicle ID: ")
            model = input("Enter Model Name: ")
            battery = int(input("Enter Battery Percentage: "))

            if vehicle_type == "1":
                seats = int(input("Enter Seating Capacity: "))
                vehicle = ElectricCar(vehicle_id, model, battery, seats)

            elif vehicle_type == "2":
                max_speed = int(input("Enter Max Speed: "))
                vehicle = ElectricScooter(vehicle_id, model, battery, max_speed)

            else:
                print("Invalid vehicle type")
                continue

            manager.add_vehicle(hub_name, vehicle)

        # 3. View Vehicles in Hub(UC6)
        elif choice == "3":
            hub_name = input("Enter hub name: ")
            vehicles = manager.get_vehicles_by_hub(hub_name)

            if not vehicles:
                print("No vehicles found.")
            else:
                for v in vehicles:
                    print(f"{v.vehicle_id} | {v.model} | {v.battery_percentage}%")

        # 4. Search by Hub(UC8)
        elif choice == "4":
            hub_name = input("Enter hub name: ")
            vehicles = manager.search_by_hub(hub_name)
            for v in vehicles:
                print(f"{v.vehicle_id} | {v.model} | {v.battery_percentage}%")

        # 5. Search by Battery(UC8)
        elif choice == "5":
            hub_name = input("Enter hub name: ")
            vehicles = manager.search_high_battery(hub_name)
            for v in vehicles:
                print(f"{v.vehicle_id} | {v.model} | {v.battery_percentage}%")

        # 6. Categorized View(UC9)
        elif choice == "6":
            manager.display_categorized_vehicles()

        # 7. Fleet Analytics(UC10)
        elif choice == "7":
            manager.fleet_analytics()

        # 8. Sort by Model(UC11)
        elif choice == "8":
            hub_name = input("Enter hub name: ")
            vehicles = manager.sort_by_model(hub_name)
            for v in vehicles:
                print(f"{v.vehicle_id} | {v.model}")

        # 9. Sort by Battery(UC12)
        elif choice == "9":
            hub_name = input("Enter hub name: ")
            manager.sort_by_battery_level(hub_name)
            print("Vehicles sorted by battery (High → Low)")

        # 10. Add to CSV(UC13)
        elif choice == "10":
            filename = input("Enter CSV filename: ")
            manager.save_to_csv(filename)
            print("Data saved to CSV")

        # 11. Add to JSON(UC14)
        elif choice == "11":
            filename = input("Enter JSON filename: ")
            manager.save_to_json(filename)
            print("Data saved to JSON")

        # 12. Exit
        elif choice == "12":
            print("Thank you for using Eco-Ride ")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
