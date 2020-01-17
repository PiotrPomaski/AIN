from Conversion import *
from Functions_and_Fittnes import FunctionsAndFittnes
from Genetic_Operator import GeneticOperator
from Roulette_Wheel import RuletteWheele
from Tournament_Selection import TournamentSelection
import math


class GeneticAlgorithm:
    average = []
    best = []
    iter_best = []
    iter_avg = []
    best_ = []
    avg_ = []
    dev_avg_ = []
    dev_best_ = []
    current_min_chromosoem = []

    def __init__(self, number_iter, population, generation_number, selection_type, precision, cros, mut, function, n,
                 interval,
                 seed_):
        self.number_iter = number_iter
        self.popu = population
        self.generation_number = generation_number
        self.selection_type = selection_type
        self.precision = precision
        self.cros = cros
        self.mut = mut
        self.function = function
        self.n = n
        interval = interval.split(';')
        self.A = float(interval[0])
        self.B = float(interval[1])
        self.seed = int(seed_)
        if self.seed != -1:
            random.seed(self.seed)

        self.chromosome_length = Conversion.variable_length(self.A, self.B, self.precision)
        self.start()

    def get_best(self):
        return self.best

    def get_average(self):
        return self.average

    def start(self):
        for iterator in range(0, self.number_iter):
            self.population = self.create_populations()
            licznik = 0
            while licznik < self.generation_number:
                print("Populacja nr {}\n".format(licznik+1), self.population)
                # Tworzenie Fitnesu
                self.create_fitness()
                # Zamiana na binarne
                self.toBinary()
                # Selekcja
                if self.selection_type == 0:
                    # Koło ruletki
                    self.rulette_wheele()
                elif self.selection_type == 1:
                    # Turniejowa
                    self.tournament_selection(2)
                elif self.selection_type == 2:
                    # Turniejowa
                    self.tournament_selection(3)
                elif self.selection_type == 3:
                    # Turniejowa
                    self.tournament_selection(4)
                elif self.selection_type == 4:
                    # Turniejowa
                    self.tournament_selection(5)

                # Krzyżowanie
                self.crossover()
                # Mutacja
                self.mutation()
                # Rozłącz na pojedyńcze punkty
                self.split_chromosome()
                licznik = licznik + 1
                self.get_best()
                self.get_average()

                # chromosome_fitness = []
                # for chromosome in self.population:
                #     if self.function == 0:
                #         r = FunctionsAndFittnes.rosenbrock(chromosome)
                #     elif self.function == 1:
                #         r = FunctionsAndFittnes.sphere(chromosome)
                #     elif self.function == 2:
                #         r = FunctionsAndFittnes.shekels_foxholes(chromosome, self.n)
                #     current = chromosome[:]
                #     current.append(r)
                #     chromosome_fitness.append(current)
                #
                # self.current_min_chromosoem = Conversion.get_min_from_list_in_list(chromosome_fitness)
                # print(self.current_min_chromosoem )

            a = self.average[:]
            b = self.best[:]
            self.iter_avg.append(a)
            self.iter_best.append(b)
            self.average = []
            self.best = []

        self.best_ = (self.get_avg(self.iter_best))
        self.avg_ = (self.get_avg(self.iter_avg))

        # b = []
        # for best in self.best_:
        #     b.append(round(best, self.precision))
        # self.best_ = b
        # a = []
        # for avg in self.avg_:
        #     a.append(round(avg, self.precision))
        # self.avg_ = a
        Conversion.save_best_and_avg(self)

    def get_avg(self, list):
        avg = []

        for x in range(0, len(list[0])):
            suma = 0
            for t in range(0, len(list)):
                suma = suma + (list[t][x])
            avg.append(suma / len(list))
        return avg

    def get_best(self):
        min_ = []
        for i in self.population:
            if self.function == 0:
                r = FunctionsAndFittnes.rosenbrock(i)
            elif self.function == 1:
                r = FunctionsAndFittnes.sphere(i)
            min_.append(r)

        self.best.append(min(min_))

    def get_average(self):
        suma = 0
        for i in self.population:
            if self.function == 0:
                suma = suma + FunctionsAndFittnes.rosenbrock(i)
            elif self.function == 1:
                suma = suma + FunctionsAndFittnes.sphere(i)
        avg = suma / len(self.population)
        self.average.append(avg)

    def split_chromosome(self):
        split_population = []
        for i in self.population:
            split_population.append(Conversion.split_multi_variable(i, self.n))

        new_population = []
        for i in split_population:
            x = []
            for j in i:
                x.append(Conversion.to_decimal(j, self.A, self.B, self.chromosome_length, self.precision))
            new_population.append(x)

        self.population = new_population

    def mutation(self):
        mut = []
        for i in self.population:
            mut.append(GeneticOperator.mutation(i, self.mut))
        self.population = mut

    def crossover(self):
        c = []
        after_crossover = []
        for i in self.population:
            r = random.random()
            if r <= self.cros:
                c.append(i)
        if len(c) < len(self.population):
            for i in range((len(self.population) - len(c))):
                r = random.randint(0, len(c) - 1)
                c.append(c[r])

        unpaired = False
        if len(c) % 2 != 0:  # musi być parzyscie do krzyżowania
            c.append(c[0])
            unpaired = True

        ax = c[:len(c) // 2]
        ay = c[len(c) // 2:]
        for i in range(0, len(ax)):
            o1, o2 = GeneticOperator.crossover(ax[i], ay[i])
            after_crossover.append(o1)
            after_crossover.append(o2)
        if unpaired:  # Do krzyżowania jest potrzerbna parzysta liczba osobników, ale nie może być ich po krzyżowaniu więcej niż N_ więc usuwamy ostatniego
            del after_crossover[-1]
            unpaired = False

        self.population = after_crossover

    def rulette_wheele(self):
        r = RuletteWheele(self.population)
        self.population = r.get_chosen()

    def tournament_selection(self, k):
        ts = TournamentSelection(self.population, k)
        after_ts = ts.tournament()
        self.population = after_ts

    def toBinary(self):
        bin_population = []
        for i in self.population:
            t = []

            for j in i[:self.n]:
                t.append(Conversion.to_binary(j, self.A, self.B, self.chromosome_length))
            b = Conversion.connect_multi_variable(t)
            t = []
            t.append(b)
            t.append(i[-1])
            bin_population.append(t)
        self.population = bin_population

    def create_fitness(self):
        for i in self.population:
            if self.function == 0:
                fitness = 1 / FunctionsAndFittnes.rosenbrock(i)
            elif self.function == 1:
                fitness = 1 / FunctionsAndFittnes.sphere(i)
            i.append(fitness)

    def create_populations(self):
        population = []
        for i in range(self.popu):
            variables = []
            for j in range(0, self.n):
                r = Conversion.rand_precision_range(self.precision, self.A, self.B)
                variables.append(r)
            population.append(variables)
        return population

    def avg(self, list):
        suma = 0
        for i in list:
            suma = suma + i
        avg = suma / len(list)
        return avg
    
    def standard_deviation(self, list):
        avg = self.avg(list)
        std_dv = 0
        for i in list:
            std_dv = std_dv + pow(i-avg, 2)
        std_dv = std_dv/(len(list)-1)
        std_dv = math.sqrt(std_dv)
        return std_dv
