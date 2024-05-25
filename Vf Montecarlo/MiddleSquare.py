import secrets
import numpy as np
import scipy.stats as stats


class MiddleSquare:
    def __init__(self, min_val, max_val, num_to_generate):
        self.seed = secrets.randbits(64)
        self.min = min_val
        self.max = max_val
        self.num_to_generate = num_to_generate
        self.generated_numbers = (
            []
        )  # Lista para almacenar los números generados por generate_ri
        self.current_index = 0  # Índice actual del número generado

    def generate_ri(self):
        generated_numbers = []
        for _ in range(self.num_to_generate):
            square = self.seed * self.seed
            square_str = str(square).zfill(12)
            size = len(square_str)
            start = (size - 8) // 2
            end = start + 4
            number_str = square_str[start:end]
            number = int(number_str) / 10000.0
            self.seed = int(square_str[2:10])
            generated_numbers.append(number)  # Agregar el número generado a la lista
        self.generated_numbers.extend(
            generated_numbers
        )  # Extender la lista de números generados
        return generated_numbers

    def pass_all_tests(self):
        generated_numbers = self.generate_ri()

        # Prueba de medias
        means_test = np.mean(generated_numbers)
        if means_test < self.min or means_test > self.max:
            return False

        # Prueba de varianza
        var_test = np.var(generated_numbers)
        if var_test < (self.max - self.min) / 12:
            return False

        # Prueba de Chi2
        chi2_test = stats.chisquare(generated_numbers)
        if chi2_test.pvalue < 0.05:
            return False

        # Prueba de KS
        ks_test = stats.kstest(generated_numbers, "uniform")
        if ks_test.pvalue < 0.05:
            return False

        # Prueba de Poker
        def poker_test(numbers):
            digits = np.array([int(str(num)[2]) for num in numbers])
            unique, counts = np.unique(digits, return_counts=True)
            observed_frequencies = counts / len(digits)
            expected_frequency = 1 / 10
            chi2_stat = np.sum(
                (observed_frequencies - expected_frequency) ** 2 / expected_frequency
            )
            critical_value = stats.chi2.ppf(0.95, 9)
            return chi2_stat < critical_value

        if not poker_test(generated_numbers):
            return False

        return True

    def generate_valid_numbers(self):
        while True:
            if self.pass_all_tests():
                # print("Los números generados son válidos.")
                # print(self.generated_numbers)
                return self.generated_numbers
            else:
                self.generated_numbers = []
                self.seed = secrets.randbits(64)
                # print("Los números generados NO son válidos.")

    def next_number(self):
        if self.current_index < len(self.generated_numbers):
            number = self.generated_numbers[self.current_index]
            self.current_index += 1
            return number
        else:
            self.generated_numbers = (
                self.generate_valid_numbers()
            )  # Regenerar la lista de números válidos
            self.reset_index()  # Reiniciar el índice para comenzar desde el principio
            return (
                self.next_number()
            )  # Llamar recursivamente para obtener el primer número de la nueva lista

    def reset_index(self):
        self.current_index = 0


if __name__ == "__main__":
    min_val = 0
    max_val = 1
    num_to_generate = 100

    middle_square = MiddleSquare(min_val, max_val, num_to_generate)

    # Generar números válidos y mostrarlos

    generated_numbers = middle_square.generate_valid_numbers()
    print("Generated Numbers:")
    print(generated_numbers)
    for i in range(num_to_generate):
        print(middle_square.next_number())
