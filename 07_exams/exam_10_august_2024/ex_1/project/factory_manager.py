from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        product_dict = {"Chair": Chair, "HobbyHorse": HobbyHorse}
        if product_type not in product_dict.keys():
            raise Exception("Invalid product type!")
        product = product_dict[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        store_info = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}
        if store_type not in store_info.keys():
            raise Exception(f"{store_type} is an invalid type of store!")
        store = store_info[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store, *products):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        filtered_products = [p for p in products if p.sub_type.lower() in store.store_type.lower()]
        if not filtered_products:
            return f"Products do not match in type. Nothing sold."

        for product in filtered_products:
            store.products.append(product)
            self.products.remove(product)
            store.capacity -= 1
            self.income += product.price
        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        store = self._find_store_name(store_name)
        if not store:
            raise Exception("No such store!")
        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        filtered_products = [p for p in self.products if p.model == product_model]
        [p.discount() for p in filtered_products]
        return f"Discount applied to {len(filtered_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = self._find_store_name(store_name)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        product_counts_per_model = {}
        total_price = 0.0
        for product in self.products:
            product_counts_per_model[product.model] = product_counts_per_model.get(product.model, 0) + 1
            total_price += product.price

        stats = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}"
        ]
        for model in sorted(product_counts_per_model.keys()):
            stats.append(f"{model}: {product_counts_per_model[model]}")

        stats.append(f"***Partner Stores: {len(self.stores)}***")
        for store in sorted(self.stores, key=lambda s: s.name):
            stats.append(store.name)

        return "\n".join(stats).strip()

    #helping_methods
    def _find_store_name(self, store_name):
        return next((s for s in self.stores if s.name == store_name), None)
