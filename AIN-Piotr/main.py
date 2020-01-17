import sys

import ctypes

from GUI import *

if __name__ == '__main__':
    user32 = ctypes.windll.user32
    user32 = ctypes.windll.user32
    szerokosc = user32.GetSystemMetrics(0) - 150
    wysokosc = user32.GetSystemMetrics(1) - 200
    app = QApplication(sys.argv)
    main = Window()
    main.setWindowTitle("Optymalizacja funkcji wielu zmiennych za pomocą algorytmu genetycznego")
    main.setGeometry(user32.GetSystemMetrics(0) / 2 - szerokosc / 2, user32.GetSystemMetrics(1) / 2 - wysokosc / 2,
                     szerokosc, wysokosc)
    main.show()
    sys.exit(app.exec_())
