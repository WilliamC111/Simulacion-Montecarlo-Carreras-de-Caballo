from MiddleSquare import MiddleSquare
import breed
import age
import rider


class Horse:
    def __init__(self, name, id_horse):
        self.generator = MiddleSquare(0, 1, 1000)
        self.name = name
        self.id_horse = id_horse
        self.breed_instance = breed.Breed()
        self.breed = self.breed_instance.determine_breed()
        self.initial_speed = self.assign_initial_speed()
        self.strength = self.assign_strength()
        self.age_instance = age.Age()
        self.age = self.age_instance.determine_age()
        self.stamina = self.assign_stamina()
        self.agility = self.assign_agility()
        self.rider_instance = rider.Rider()
        self.rider_experience = self.rider_instance.determine_experience()
        self.balance = self.assign_balance()
        self.speed = self.calculate_speed()
        self.recover_initial_speed = self.initial_speed
        self.recover_speed = self.speed
        self.recover_strength = self.strength
        self.recover_stamina = self.stamina
        self.recover_agility = self.agility
        self.recover_balance = self.balance
        self.winning_races = 0

    def assign_initial_speed(self):
        porcentajes = self.breed_instance.get_porcentajes_initial_speed(self.breed)
        random_number = self.generator.next_number()
        if random_number <= porcentajes[0]:
            return self.generate_Ni(1, 4)
        elif random_number <= porcentajes[1]:
            return self.generate_Ni(5, 8)
        elif random_number <= porcentajes[2]:
            return self.generate_Ni(9, 12)
        elif random_number <= porcentajes[3]:
            return self.generate_Ni(13, 16)

    def assign_strength(self):
        porcentajes = self.breed_instance.get_porcentajes_strength(self.breed)
        random_number = self.generator.next_number()
        if random_number <= porcentajes[0]:
            return self.generate_Ni(1, 4)
        elif random_number <= porcentajes[1]:
            return self.generate_Ni(5, 8)
        elif random_number <= porcentajes[2]:
            return self.generate_Ni(9, 12)
        elif random_number <= porcentajes[3]:
            return self.generate_Ni(13, 16)

    def assign_stamina(self):
        porcentajes = self.age_instance.get_porcentajes_stamina(self.age)
        random_number = self.generator.next_number()
        if random_number <= porcentajes[0]:
            return self.generate_Ni(1, 4)
        elif random_number <= porcentajes[1]:
            return self.generate_Ni(5, 8)
        elif random_number <= porcentajes[2]:
            return self.generate_Ni(9, 12)
        elif random_number <= porcentajes[3]:
            return self.generate_Ni(13, 16)

    def assign_agility(self):
        porcentajes = self.age_instance.get_porcentajes_agility(self.age)
        random_number = self.generator.next_number()
        if random_number <= porcentajes[0]:
            return self.generate_Ni(1, 4)
        elif random_number <= porcentajes[1]:
            return self.generate_Ni(5, 8)
        elif random_number <= porcentajes[2]:
            return self.generate_Ni(9, 12)
        elif random_number <= porcentajes[3]:
            return self.generate_Ni(13, 16)

    def assign_balance(self):
        porcentajes = self.rider_instance.get_porcentajes_balance(self.rider_experience)
        random_number = self.generator.next_number()
        if random_number <= porcentajes[0]:
            return self.generate_Ni(1, 4)
        elif random_number <= porcentajes[1]:
            return self.generate_Ni(5, 8)
        elif random_number <= porcentajes[2]:
            return self.generate_Ni(9, 12)
        elif random_number <= porcentajes[3]:
            return self.generate_Ni(13, 16)

    def generate_Ni(self, max, min):
        return (max - min) * self.generator.next_number() + min

    def calculate_speed(self):
        if self.strength < 0:
            self.strength = 0
        if self.stamina < 0:
            self.stamina = 0
        if self.agility < 0:
            self.agility = 0
        if self.balance < 0:
            self.balance = 0
        speed = round(
            (self.initial_speed * 0.4)
            + (self.strength * 0.22)
            + (self.stamina * 0.17)
            + (self.agility * 0.13)
            + (self.balance * 0.08),
            3,
        )
        if speed < 0:
            speed = 0
        return speed

    def recover_horse(self):
        self.speed = self.recover_speed
        self.strength = self.recover_strength
        self.stamina = self.recover_stamina
        self.agility = self.recover_agility
        self.balance = self.recover_balance
        self.initial_speed = self.recover_initial_speed

    def decrease_attribute(self, attribute, value_speed, value):
        print(self.name)
        print(self.speed)
        if attribute == "strength":
            self.strength -= value
            self.initial_speed -= value_speed
        elif attribute == "stamina":
            self.stamina -= value
            self.initial_speed -= value_speed
        elif attribute == "agility":
            self.agility -= value
            self.initial_speed -= value_speed
        else:
            print("Invalid attribute")
        self.speed = self.calculate_speed()
        print(self.speed)

    def add_winning_races(self):
        self.winning_races += 1

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_initial_speed(self):
        return self.initial_speed

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_strength(self):
        return self.strength

    def get_age(self):
        return self.age

    def get_stamina(self):
        return self.stamina

    def get_agility(self):
        return self.agility

    def get_rider_experience(self):
        return self.rider_experience

    def get_balance(self):
        return self.balance

    def get_winning_races(self):
        return self.winning_races

    def get_id_horse(self):
        return self.id_horse


def main():
    n = 10  # Number of horses to create
    horses = []

    for i in range(n):
        name = f"Horse {i+1}"
        id_horse = i + 1
        horse = Horse(name, id_horse)
        horses.append(horse)

    # Print the details of each horse
    for horse in horses:
        print(
            f"Name: {horse.name}, Breed: {horse.breed}, Initial_Speed: {horse.initial_speed}, Strength: {horse.assign_strength()},age: {horse.age}, Stamina: {horse.stamina}, Agility: {horse.agility}, Rider experience: {horse.rider_experience} , Balance: {horse.balance} , Speed : {horse.speed}"
        )


if __name__ == "__main__":
    main()
