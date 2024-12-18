from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant
from collections import Counter


class FlowerShopManager:
    VALID_PLANTS = {
        "Flower": Flower,
        "LeafPlant": LeafPlant
    }
    VALID_CLIENTS = {
        "RegularClient": RegularClient,
        "BusinessClient": BusinessClient
    }

    def __init__(self):
        self.income = 0.0
        self.plants = [] #all plants objects the shop has
        self.clients = [] #all clients objects the shop has

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.VALID_PLANTS:
            raise ValueError("Unknown plant type!")
        new_plant = self.VALID_PLANTS[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.VALID_CLIENTS:
            raise ValueError("Unknown client type!")
        try:
            client = [c for c in self.clients if c.phone_number == client_phone_number][0]
            raise ValueError("This phone number has been used!")
        except IndexError:
            new_client = self.VALID_CLIENTS[client_type](client_name, client_phone_number)
            self.clients.append(new_client)
            return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        try:
            client = [c for c in self.clients if c.phone_number == client_phone_number][0]
        except IndexError:
            raise ValueError("Client not found!")

        plants = [p for p in self.plants if p.name == plant_name]
        if not plants:
            raise ValueError("Plants not found!")
        if len(plants) < plant_quantity:
            return "Not enough plant quantity."

        plants_for_sale = plants[:plant_quantity]

        order_amount = 0.0
        for plant in plants_for_sale:
            if plant in self.plants:
                order_amount += plant.price - (plant.price * client.discount / 100)
                self.plants.remove(plant)

        self.income += order_amount
        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name: str):
        try:
            plant = [p for p in self.plants if p.name == plant_name][0]
            self.plants.remove(plant)
            return f"Removed {plant.plant_details()}"
        except IndexError:
            return "No such plant name."

    def remove_clients(self):
        zero_clients = [c for c in self.clients if c.total_orders == 0]
        for client in zero_clients:
            if client in self.clients:
                self.clients.remove(client)
        return f"{len(zero_clients)} client/s removed."

    def shop_report(self):
        plant_name_count = Counter(plant.name for plant in self.plants)

        sorted_plants = sorted(self.plants, key=lambda plant: (-plant_name_count[plant.name], plant.name))
        sorted_clients = (client.client_details() for client in
                          sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number)))

        result = f"~Flower Shop Report~\nIncome: {self.income:.2f}\nCount of orders: {sum([c.total_orders for c in self.clients])}\n~~Unsold plants: {len(self.plants)}~~\n"

        sorted_plants_counts = Counter(plant.name for plant in sorted_plants)
        for plant_name, count in sorted_plants_counts.items():
            result += f'{plant_name}: {count}\n'

        result += f'~~Clients number: {len(self.clients)}~~\n'
        for client in sorted_clients:
            result += f'{client}\n'

        return result.strip()
