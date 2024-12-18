from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    VALID_TYPES_OF_SUPPLIES = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        players_added = []
        for player in args:
            if player not in self.players:
                players_added.append(player)
                self.players.append(player)
        return f"Successfully added: {', '.join(p.name for p in players_added)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self.VALID_TYPES_OF_SUPPLIES:
            return
        # TO DO
        try:
            player = [p for p in self.players if p.name == player_name][0]
        except IndexError:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) - 1, -1, -1):
            current_supply = self.supplies[i]

            if current_supply.__class__.__name__ == sustenance_type:
                self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player.stamina + current_supply.energy > 100:
            player.stamina = 100
        else:
            player.stamina += current_supply.energy

        return f"{player_name} sustained successfully with {current_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        current_player = sorted(
            (
                [p for p in self.players if first_player_name == p.name][0],
                [p for p in self.players if second_player_name == p.name][0]
            ), key=lambda p: p.stamina
        )
        errors_list = []

        for player in current_player:
            if player.stamina <= 0:
                errors_list.append(f"Player {player.name} does not have enough stamina.")

        if errors_list:
            return "\n".join(errors_list)

        return self.fight(current_player)

    def fight(self, current_player):
        first_player_damage = current_player[0].stamina / 2

        if current_player[1].stamina <= first_player_damage:
            current_player[1].stamina = 0
            return f"Winner: {current_player[0].name}"
        else:
            current_player[1].stamina -= first_player_damage

        second_player_damage = current_player[1].stamina / 2

        if current_player[0].stamina <= second_player_damage:
            current_player[0].stamina = 0
        else:
            current_player[0].stamina -= second_player_damage

        winner = sorted(current_player, key=lambda p: -p.stamina)[0]
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            reduce_stamina_with = player.age * 2
            player.stamina = max(player.stamina - reduce_stamina_with, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}\n"
        for supply in self.supplies:
            result += f"{supply.__class__.__name__}: {supply.name}, {supply.energy}"
        return result
