from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        valid_waiters = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
        if waiter_type not in valid_waiters.keys():
            return f"{waiter_type} is not a recognized waiter type."

        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if waiter:
            return f"{waiter_name} is already on the staff."

        new_waiter = valid_waiters[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        valid_clients = {"RegularClient": RegularClient, "VIPClient": VIPClient}
        if client_type not in valid_clients.keys():
            return f"{client_type} is not a recognized client type."

        client = next((c for c in self.clients if c.name == client_name), None)
        if client:
            return f"{client_name} is already a client."

        new_client = valid_clients[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            return f"{client_name} is not a registered client."
        return f"{client_name} earned {client.earning_points(order_amount)} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        return f"{client_name} received a {client.apply_discount()[0]}% discount. Remaining points {client.apply_discount()[1]}"

    def generate_report(self):
        sorted_waiters = sorted(self.waiters, key=lambda w: -w.calculate_earnings())
        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)
        clients_count = len(self.clients)
        waiter_info = "** Waiter Details **\n"
        for waiter in sorted_waiters:
            waiter_info += f"{str(waiter)}\n"
        result = f"$$ Monthly Report $$\n" \
                 f"Total Earnings: ${total_earnings:.2f}\n" \
                 f"Total Clients Unused Points: {total_client_points}\n" \
                 f"Total Clients Count: {clients_count}\n"
        result += waiter_info
        return result.strip()
