from MiddleSquare import MiddleSquare


class Breed:
    def __init__(self):
        self.generator = MiddleSquare(0, 1, 1000)

    def determine_breed(self):
        random_number = self.generator.next_number()
        if random_number <= 0.4:
            self.breed = "PSI"
        elif random_number <= 0.6:
            self.breed = "ARABE"
        elif random_number <= 0.8:
            self.breed = "CM"
        else:
            self.breed = "APPALOOSA"
        return self.breed

    def get_porcentajes_initial_speed(self, breed):
        # Define los porcentajes para cada raza y los devuelve acumulados
        if breed == "PSI":
            # Por ejemplo, para la raza "PSI", [0.2, 0.5, 0.9, 1.0] significa que el 20% de las veces devolverá un valor en el rango de 1 a 4, el 30% de las veces devolverá un valor en el rango de 5 a 8, el 40% de las veces devolverá un valor en el rango de 9 a 12, y el 10% de las veces devolverá un valor en el rango de 13 a 16.
            return [0.08, 0.18, 0.3, 1.0]
        elif breed == "ARABE":
            return [0.21, 0.61, 0.82, 1.0]
        elif breed == "CM":
            return [0.45, 0.6, 0.9, 1.0]
        elif breed == "APPALOOSA":
            return [0.18, 0.43, 0.85, 1.0]

    def get_porcentajes_strength(self, breed):
        if breed == "PSI":
            return [0.23, 0.61, 0.82, 1.0]
        elif breed == "ARABE":
            return [0.35, 0.56, 0.8, 1.0]
        elif breed == "CM":
            return [0.12, 0.27, 0.52, 1.0]
        elif breed == "APPALOOSA":
            return [0.23, 0.59, 0.84, 1.0]
