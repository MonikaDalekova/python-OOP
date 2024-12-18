from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar

vehicle_types = {
    "PassengerCar": PassengerCar,
    "CargoVan": CargoVan
}


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def define_route_id(self):
        return len(self.routes) + 1

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            existing_user = [user for user in self.users if driving_license_number == user.driving_license_number][0]
            return f"{driving_license_number} has already been registered to our platform."
        except IndexError:
            user = User(first_name, last_name, driving_license_number)
            self.users.append(user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        try:
            existing_vehicle = [v for v in self.vehicles if license_plate_number == v.license_plate_number][0]
            return f"{license_plate_number} belongs to another vehicle."
        except IndexError:
            v = vehicle_types[vehicle_type](brand, model, license_plate_number) #инстанциране на класа
            self.vehicles.append(v)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        try:
            greater_length_route = [r for r in self.routes if r.start_point == start_point
                     and r.end_point == end_point and r.length > length][0]
            greater_length_route.is_locked = True
        except IndexError:
            pass

        try:
            route = [r for r in self.routes if r.start_point == start_point
                     and r.end_point == end_point and r.length < length][0]
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."
        except IndexError:
            try:
                route = [r for r in self.routes if r.start_point == start_point
                         and r.end_point == end_point and r.length == length][0]
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            except IndexError:
                r_id = self.define_route_id()
                r = Route(start_point, end_point, length, r_id)
                self.routes.append(r)
                return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        route = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length) #start driving

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles_list = [v for v in self.vehicles if v.is_damaged]
        damaged_vehicles = sorted(vehicles_list, key=lambda v: (v.brand, v.model))
        if len(damaged_vehicles) > count:
            damaged_vehicle_to_be_repaired = damaged_vehicles[:count]
            for v in damaged_vehicle_to_be_repaired:
                v.is_damaged = False
                v.recharge()
            return f"{len(damaged_vehicle_to_be_repaired)} vehicles were successfully repaired!"

    def users_report(self):
        ordered_users = sorted(self.users, key=lambda u: -u.rating)
        result = "*** E-Drive-Rent ***\n"

        result += "\n".join([str(u) for u in ordered_users])

        return result
