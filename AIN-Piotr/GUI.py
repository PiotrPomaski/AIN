import ctypes
import tkinter as tk
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Functions_and_Fittnes import FunctionsAndFittnes
from Genetic_Algorithm import GeneticAlgorithm

from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plot


class FunctionWindow(QDialog):
    def __init__(self, parent=None):
        super(FunctionWindow, self).__init__(parent)


class Window(QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.start = QPushButton('Start')
        #self.restart = QPushButton("Resetuj")
        #self.restart.clicked.connect(self.plot())
        self.start.clicked.connect(self.startAG)

        self.show_function = QPushButton('Podgląd funkcji')
        self.show_function.clicked.connect(self.show_f)

        self.iter_text = QLabel("Ilość uruchomień AG:")
        self.iter = QLineEdit()
        self.iter.setText("1")

        #self.ag = QLabel("Ustawienia AG")
        #self.f_ = QLabel("Ustawienia funkcji")
        self.text_N = QLabel("Rozmiar populacji")
        self.text_n = QLabel("Ilość zmiennych")
        self.text_generation_number = QLabel("Liczba generacji")
        self.text_selection = QLabel("Typ selekcji")
        self.text_precision = QLabel("Precyzja wyniku")
        self.text_cros = QLabel("Prawdopodobieństow krzyżowania")
        self.text_mut = QLabel("Prawdopodobieństow mutacji")
        self.text_function = QLabel("Funkcja")
        self.text_interval = QLabel("Przedział")
        self.text_seed = QLabel("Ziarno")
        self.informacje = QLabel("")
        #self.ag.setStyleSheet("font: 10pt")
        #self.ag.setAlignment(Qt.AlignCenter)
        #self.f_.setStyleSheet("font: 10pt")
        #self.f_.setAlignment(Qt.AlignCenter)

        # Ustawienie funkci
        self.function = QComboBox()
        self.function.addItem("Rosenbrock")
        self.function.addItem("Sphere")


        # Typ selekcji
        self.selection_type = QComboBox()
        self.selection_type.addItem("Selekcja proporcjonalna")
        self.selection_type.addItem("Seleckja Turniejowa k=2")
        self.selection_type.addItem("Seleckja Turniejowa k=3")
        self.selection_type.addItem("Seleckja Turniejowa k=4")
        self.selection_type.addItem("Seleckja Turniejowa k=5")

        # Prawdopoodbieństwo i mutacja
        self.cros = QLineEdit()
        self.cros.setText("0.9")
        self.mut = QLineEdit()
        self.mut.setText("0.01")

        # Dokładność wyniku
        self.precision = QComboBox()
        self.precision.addItem("10 do -2")
        self.precision.addItem("10 do -3")
        self.precision.addItem("10 do -4")
        self.precision.addItem("10 do -5")
        self.precision.addItem("10 do -6")

        # Liczba generacji
        self.generation_number = QLineEdit()
        self.generation_number.setText("200")

        # Rozmiar populacji
        self.population = QLineEdit()
        self.population.setText("100")

        # Ilosć zmiennych
        self.n = QLineEdit()
        self.n.setText("2")

        # Przedział funkcji
        self.interval = QLineEdit()
        self.interval.setText("-2.5;3")

        # Ziarno
        self.seedW = QLineEdit()

        menu = QVBoxLayout()
        splitter1 = QSplitter(Qt.Vertical)
        menu.addWidget(splitter1)
        menu.addWidget(splitter1)
        #splitter1.addWidget(self.ag)
        splitter1.setSizes([1, 2])

        menu.addWidget(self.iter_text)
        menu.addWidget(self.iter)
        menu.addWidget(self.text_seed)
        menu.addWidget(self.seedW)

        #menu.addWidget(self.ag)

        menu.addWidget(self.text_N)
        menu.addWidget(self.population)

        menu.addWidget(self.text_generation_number)
        menu.addWidget(self.generation_number)

        menu.addWidget(self.text_selection)
        menu.addWidget(self.selection_type)

        menu.addWidget(self.text_precision)
        menu.addWidget(self.precision)

        menu.addWidget(self.text_cros)
        menu.addWidget(self.cros)

        menu.addWidget(self.text_mut)
        menu.addWidget(self.mut)

        menu.addWidget(splitter1)

        #menu.addWidget(self.f_)
        menu.addWidget(self.text_function)
        menu.addWidget(self.function)
        menu.addWidget(self.show_function)
        menu.addWidget(self.text_n)
        menu.addWidget(self.n)
        menu.addWidget(self.text_interval)
        menu.addWidget(self.interval)

        #menu.addWidget(self.sl)
        menu.addWidget(self.start)

        splitter1 = QSplitter(Qt.Vertical)
        menu.addWidget(splitter1)
        menu.addWidget(splitter1)
        #splitter1.addWidget(self.ag)

        splitter1.setSizes([1, 2])

        wykres = QVBoxLayout()

        wykres.addWidget(self.toolbar)
        wykres.addWidget(self.canvas)

        layout = QHBoxLayout()
        layout.addLayout(menu, 20)
        layout.addLayout(wykres, 80)

        self.setLayout(layout)
        self.show()

    def show_f(self):
        self.SW = PlotWindow(self.function.currentIndex())
        self.SW.show()

    def startAG(self):
        print("Population:", self.population.text())
        print("Generation Number: ", self.generation_number.text())
        print("Selection: ", self.selection_type.currentIndex(), " ", self.selection_type.currentText())
        print("Precision: ", self.precision.currentIndex() + 2)
        print("Crossover: ", self.cros.text())
        print("Mutation: ", self.mut.text())
        print("Function: ", self.function.currentIndex())
        print("n: ", self.n.text())
        print("Interval: ", self.interval.text())
        print("Doszło #-1")
        print("Seed: ", self.seedW.text())
        print("Doszło #0")

        if self.seedW.text() == "":
            self.seed = "-1"
        else:
            self.seed = int(self.seedW.text())


        self.ga = GeneticAlgorithm(int(self.iter.text()), int(self.population.text()), int(self.generation_number.text()),
                              self.selection_type.currentIndex(),
                              self.precision.currentIndex() + 2, float(self.cros.text()),
                              float(self.mut.text()),
                              int(self.function.currentIndex()), int(self.n.text()), self.interval.text(),
                              self.seed)
        self.plot(list(range(1, len(self.ga.avg_) + 1)), self.ga.avg_, list(range(1, len(self.ga.best_) + 1)), self.ga.best_, self.ga.dev_avg_, self.ga.dev_best_)

    def plot(self, x1, y1, x2, y2, d1, d2):
        plt.clf()
        root = tk.Tk()
        root.withdraw()

        #plt.subplot(2, 1, 2)
        plt.plot(x1, y1, "r")
        if len(self.ga.iter_best) > 1:
            plt.errorbar(x1, y1, d1, linestyle='None')
        #plt.plot(x2, y2, "c")
        #if len(self.ga.iter_best) > 1:
        #    plt.errorbar(x2, y2, d2, linestyle='None')
        plt.xlabel('Numer generacji')
        plt.ylabel('Najlepszy osobnik \ Średnia osobników')
        #plt.subplot(2, 1, 2)
        plt.plot(x2, y2, "c")
        #plt.xlabel('Numer generacji')
        #plt.ylabel('Najlepszy osobnik')

        self.canvas.draw()



class PlotWindow(QWidget):

    def __init__(self, function):
        super().__init__()
        self.function = function
        user32 = ctypes.windll.user32
        szerokosc = 640
        wysokosc = 480

        self.title = 'Podgląd wybranej funkcji'
        self.left = user32.GetSystemMetrics(0) / 2 - szerokosc / 2
        self.top = user32.GetSystemMetrics(1) / 2 - wysokosc / 2
        self.width = szerokosc
        self.height = wysokosc
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)

        function_image = None
        if self.function == 0:
            function_image = QPixmap('r.png')
        elif self.function == 1:
            function_image = QPixmap('s.png')

        label.setPixmap(function_image)
        self.resize(function_image.width(), function_image.height())


        self.show()
