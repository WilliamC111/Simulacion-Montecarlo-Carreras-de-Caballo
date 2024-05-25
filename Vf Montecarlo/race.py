from MiddleSquare import MiddleSquare
import horse
from horse import Horse

class Race:
    def __init__(self, horses: list[horse.Horse], code: int):
        self.generator = MiddleSquare(0, 1, 1000)
        self.weather = self.determine_weather()
        self.horses = horses
        self.code = code
        self.determine_event()
        self.winner = self.winnigs_horse()

    def determine_weather(self):
        random_number = self.generator.next_number()
        if random_number <= 0.5:
            self.weather = "wet"
        else:
            self.weather = "dry"
        return self.weather

    def winnigs_horse(self) -> horse.Horse:
        winning_horse = None
        max_speed = 0
        for horse in self.horses:
            if horse.get_speed() > max_speed:
                max_speed = horse.get_speed()
                winning_horse = horse
        winning_horse.add_winning_races()
        return winning_horse

    def get_horses(self) -> list[horse.Horse]:
        return self.horses

    def weather_wet(self):
        print("Entro en wet")
        random = self.generator.next_number()
        if 0 < random <= 0.09:
            self.fatigue()
        elif 0.1 < random <= 0.17:
            self.insolation()
        elif 0.2 < random <= 0.28:
            self.dehydration()
        elif 0.53 < random <= 0.43:
            self.muddy()
        elif 0.8 < random <= 0.6:
            self.fog()
        elif 0.9 < random <= 0.95:
            self.rain()
        elif 0.95 < random <= 1:
            self.drop()

    def weather_dry(self):
        print("Entro en dry")
        random = self.generator.next_number()
        if 0 < random <= 0.13:
            self.fatigue()
        elif 0.1 < random <= 0.3:
            self.insolation()
        elif 0.2 < random <= 0.67:
            self.dehydration()
        elif 0.53 < random <= 0.78:
            self.muddy()
        elif 0.8 < random <= 0.86:
            self.fog()
        elif 0.9 < random <= 0.95:
            self.rain()
        elif 0.95 < random <= 1:
            self.drop()

    def determine_event(self):
        return self.weather_dry() if self.weather == "dry" else self.weather_wet()

    def rain(self):
        print("Lluvia")
        id_horses = self.select_horses_to_affect()
        for horse in self.horses:
            if horse.get_id_horse() in id_horses:
                horse.decrease_attribute("stamina", 5, 9)

    def fog(self):
        print("Niebla")
        id_horses = self.select_horses_to_affect()
        for horse in self.horses:
            if horse.get_id_horse() in id_horses:
                horse.decrease_attribute("agility", 2, 12)

    def muddy(self):
        print("Lodo")
        id_horses = self.select_horses_to_affect()
        for horse in self.horses:
            if horse.get_id_horse() in id_horses:
                horse.decrease_attribute("strength", 3, 6)

    def insolation(self):
        print("Insolación")
        id_horses = self.select_horses_to_affect()
        for horse in self.horses:
            if horse.get_id_horse() in id_horses:
                horse.decrease_attribute("agility", 3, 11)

    def fatigue(self):
        print("Fatiga")
        id_horses = self.select_horses_to_affect()
        for horse in self.horses:
            if horse.get_id_horse() in id_horses:
                horse.decrease_attribute("stamina", 5, 8)

    def dehydration(self):
        print("Deshidratación")
        id_horses = self.select_horses_to_affect()
        for horse in self.horses:
            if horse.get_id_horse() in id_horses:
                horse.decrease_attribute("strength", 2, 7)

    def drop(self):
        print("caida")
        for horse in self.horses:
            if horse.get_balance() < 2 and horse.get_speed() > 16:
                random = self.generator.next_number()
                if 0 < random <= 0.25:  # 25% de probabilidad de caerse
                    horse.set_speed(0)

    def generate_Ni(self, max, min):
        return int((max - min) * self.generator.next_number() + min)

    def select_horses_to_affect(self):
        # Determina una cantidad aleatoria de caballos a afectar
        num_horses_to_affect = self.generate_Ni(11, 0)  # |
        print(f"Se afectarán {num_horses_to_affect} caballos")
        # Selecciona los caballos a afectar
        horses_to_affect = []
        horse_ids = [
            horse.get_id_horse() for horse in self.horses
        ]  # Lista con los ids de los caballos
        for i in range(0, num_horses_to_affect):
            horse_id = self.generate_Ni(11, 0)
            while (
                horse_id in horses_to_affect or horse_id not in horse_ids
            ):  # Verifica que el caballo no haya sido seleccionado previamente
                horse_id = self.generate_Ni(11, 0)
            horses_to_affect.append(horse_id)
        print(f"Los caballos a afectar son: {horses_to_affect}")
        return horses_to_affect

    def restart_horses(self):
        for horse in self.horses:
            horse.recover_horse()

    def get_weather(self) -> str:
        return self.weather

    def get_winner(self) -> horse.Horse:
        return self.winner
    
    def get_code(self):
        return self.code


def main():
    n = 10  # Number of horses to create
    horses = []

    for i in range(n):
        name = f"Horse {i+1}"
        id_horse = i + 1
        horse = Horse(name, id_horse)
        horses.append(horse)
        print(horse.get_name())
        print(horse.get_speed())
    race = Race(horses, 12345)  # Create a race with the horses and a code
    print(race.get_weather())  # Get the weather
    race.determine_event()  # Determine the event
    winner = race.winnigs_horse()  # Get the winning horse
    print(f"The winner is {winner.get_name()}!")  # Print the winner's name


if __name__ == "__main__":
    main()
