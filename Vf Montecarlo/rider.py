from MiddleSquare import MiddleSquare


class Rider:
    def __init__(self):
        self.generator = MiddleSquare(0, 1, 1000)

    def determine_experience(self):
        random_number = self.generator.next_number()
        if random_number <= 0.22:
            self.experience = "Principiante"
        elif random_number <= 0.68:
            self.experience = "Intermedio"
        else:
            self.experience = "Experto"
        return self.experience

    def get_porcentajes_balance(self, experience):
        if experience == "Principiante":
            return [0.28, 0.52, 0.74, 1.0]
        elif experience == "Intermedio":
            return [0.2, 0.52, 0.77, 1.0]
        elif experience == "Experto":
            return [0.14, 0.38, 0.59, 1.0]
