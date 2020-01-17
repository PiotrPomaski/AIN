import random


class GeneticOperator:

    @staticmethod
    def mutation(chromosome, mut):
        for i in range(0, len(chromosome) - 1):
            r = random.random()
            if r <= mut:
                binary = list(chromosome)
                if binary[i] == "1":
                    binary[i] = "0"
                else:
                    binary[i] = "1"
                chromosome = "".join(binary)
        return chromosome

    @staticmethod
    def crossover(chromosome1, chromosome2):
        if len(chromosome1) > len(chromosome2):
            r = random.randint(1, len(chromosome2) - 1)
        else:
            r = random.randint(1, len(chromosome1) - 1)

        o1 = chromosome1[:r] + chromosome2[r:]
        o2 = chromosome2[:r] + chromosome1[r:]

        return [o1, o2]
