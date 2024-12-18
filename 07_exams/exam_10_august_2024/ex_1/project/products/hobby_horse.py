from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    def __init__(self, model, price, material="Wood/Plastic", sub_type = "Toys"):
        super().__init__(model, price, material, sub_type)

    def discount(self):
        self.price -= self.price * 0.2
