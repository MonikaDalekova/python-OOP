from project.products.base_product import BaseProduct


class Chair(BaseProduct):
    def __init__(self, model, price, material="Wood", sub_type="Furniture"):
        super().__init__(model, price, material, sub_type)

    def discount(self):
        self.price -= self.price * 0.10
