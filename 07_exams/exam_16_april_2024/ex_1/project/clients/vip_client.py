from project.clients.base_client import BaseClient
import math


class VIPClient(BaseClient):
    MEMBERSHIP_TYPE = 'VIP'

    def __init__(self, name):
        super().__init__(name, self.MEMBERSHIP_TYPE)

    def earning_points(self, order_amount: float):
        earned_points = math.floor(order_amount / 5)
        self.points += earned_points
        return earned_points
