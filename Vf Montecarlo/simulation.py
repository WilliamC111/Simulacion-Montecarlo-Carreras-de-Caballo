from horse import Horse
from race import Race

class Simulation:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            number_race = kwargs.pop('number_race', None)
            cls._instance = super().__new__(cls)
            cls._instance.initialize(number_race)
        return cls._instance

    def initialize(self, number_race):
        self.number_race = number_race
        self.list_races = []
        self.horses = []
        self.init_simulations()

    def init_horses(self):
        for i in range(10):
            name = f"Horse {i+1}"
            id_horse = i + 1
            horse = Horse(name, id_horse)
            self.horses.append(horse)

    def init_simulations(self):
        self.init_horses()
        for i in range(self.number_race):
            race = Race(self.horses, i + 1)
            self.list_races.append(race)
            race.restart_horses()

    def get_list_race(self):
        return self.list_races

    def get_winner_for_race(self):
        winners = []
        for race in self.list_races:
            winner = race.get_winner()
            if winner:
                winners.append(winner)
        return winners

    def count_wins_by_race(self):
        wins = {'PSI': 0, 'ARABE': 0, 'CM': 0, 'APPALOOSA': 0}
        for race in self.list_races:
            winner = race.get_winner()
            if winner:
                wins[winner.get_breed()] += 1
        return [wins['PSI'], wins['ARABE'], wins['CM'], wins['APPALOOSA']]

    def count_wins_by_age(self):
        wins = {'Menor': 0, 'Igual': 0, 'Mayor': 0}
        for race in self.list_races:
            winner = race.get_winner()
            if winner:
                wins[winner.get_age()] += 1
        return [wins['Menor'], wins['Igual'], wins['Mayor']]

    def get_podio(self):
        sorted_horses = sorted(self.horses, key=lambda horse: horse.get_winning_races(), reverse=True)
        return sorted_horses[:3]

