from MiddleSquare import MiddleSquare


class Age:

    def __init__(self):
        self.generator = MiddleSquare(0, 1, 1000)

    def determine_age(self):
        random_number = self.generator.next_number()
        if random_number <= 0.25:
            self.age = "Menor"
        elif random_number <= 0.75:
            self.age = "Igual"
        else:
            self.age = "Mayor"
        return self.age

    def get_porcentajes_stamina(self, age):
        if age == "Menor":
            return [0.11, 0.37, 0.5, 1.0]
        elif age == "Igual":
            return [0.23, 0.56, 0.86, 1.0]
        elif age == "Mayor":
            return [0.44, 0.6, 0.82, 1.0]

    def get_porcentajes_agility(self, age):
        if age == "Menor":
            return [0.17, 0.55, 0.8, 1.0]
        elif age == "Igual":
            return [0.12, 0.3, 0.63, 1.0]
        elif age == "Mayor":
            return [0.27, 0.49, 0.82, 1.0]
