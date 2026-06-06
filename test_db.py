from database import get_all_vehicles

vehicles = get_all_vehicles()

for vehicle in vehicles:
    print(vehicle)