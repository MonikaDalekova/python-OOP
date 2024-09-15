from project.animals.animal import Mammal
from project.food import Food, Meat, Vegetable, Fruit


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def gained_weight(self):
        return 0.10

    @property
    def appropriate_food(self):
        return [Vegetable, Fruit]


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def gained_weight(self):
        return 0.40

    @property
    def appropriate_food(self):
        return [Meat]


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def gained_weight(self):
        return 0.30

    @property
    def appropriate_food(self):
        return [Meat, Vegetable]


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def gained_weight(self):
        return 1.00

    @property
    def appropriate_food(self):
        return [Meat]
