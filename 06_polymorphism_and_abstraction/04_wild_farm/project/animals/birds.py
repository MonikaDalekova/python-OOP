from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def gained_weight(self):
        return 0.25

    @property
    def appropriate_food(self):
        return [Meat]


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def gained_weight(self):
        return 0.35

    @property
    def appropriate_food(self):
        return [Meat, Vegetable, Fruit, Seed]