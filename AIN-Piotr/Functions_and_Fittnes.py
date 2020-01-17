import matplotlib

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plot


class FunctionsAndFittnes():

    @staticmethod
    def sphere(x):
        suma = 0
        for i in x:
            suma = suma + pow(i, 2)
        if suma == 0:
            suma = 0.00000000000000001
        return suma

    def sphere_(x):
        suma = 0
        for i in x:
            suma = suma + pow(i, 2)
        return suma

    @staticmethod
    def rosenbrock(x):
        suma = 0
        for i in range(0, len(x) - 1):
            suma = suma + 100.0 * (x[i + 1] - x[i] ** 2.0) ** 2.0 + (1 - x[i]) ** 2.0
        if suma <= 0:
            suma = 0.00000000000000000000000001
        return suma

    @staticmethod
    def rosenbrock_(x):
        suma = 0
        for i in range(0, len(x) - 1):
            suma = suma + 100.0 * (x[i + 1] - x[i] ** 2.0) ** 2.0 + (1 - x[i]) ** 2.0

        return suma


    @staticmethod
    def show_function(fun):
        fig = plot.figure()
        ax = fig.gca(projection='3d')
        X = None
        Y = None
        Z = None
        if fun == 1:
            s = 1
            X = np.arange(-10, 10. + s, s)
            Y = np.arange(-10, 10. + s, s)
            X, Y = np.meshgrid(X, Y)
            Z = FunctionsAndFittnes.sphere([X, Y])
        elif fun == 0:
            s = 0.1
            X = np.arange(-2, 2. + s, s)
            Y = np.arange(-1, 3. + s, s)
            X, Y = np.meshgrid(X, Y)
            Z = FunctionsAndFittnes.rosenbrock([X, Y])


        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, norm=LogNorm(), cmap=cm.jet)



        plt.show()



