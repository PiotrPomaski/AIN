import random


class RuletteWheele:
    chromosomes = []

    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.get_probability()

    def get_probability(self):
        suma = 0
        for i in self.chromosomes:
            suma = suma + i[-1]
        total_fit = float(suma)

        for i in self.chromosomes:
            i[-1] = i[-1] / total_fit


    def roulette_wheel_pop(self):
        chosen = []
        chosen.append(self.min_value()[0])
        while True:
            for i in self.chromosomes:
                if len(chosen) == len(self.chromosomes):
                    return chosen
                r = random.random()
                if r <= i[-1]:
                    chosen.append(i[0])


    def get_chosen(self):
        return self.roulette_wheel_pop()

    def min_value(self):
        max_ = max([sublist[-1] for sublist in self.chromosomes])
        best = ([sublist for sublist in self.chromosomes if max_ == sublist[-1]])

        return best[0]
