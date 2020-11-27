import numpy as np
from main import matrix, population, br

# obliczanie wsp_dos i wpisywanie do macierzy
def wsp_dost():
    wsp_dos = []
    for i in range(len(matrix)):
        # Mnożenie
        test = np.multiply(matrix[i], population)
        # sumowanie wiersza
        b = np.sum(test, axis=1)
        wsp_dos.append(sum(abs(b - br)))
    return np.array(wsp_dos)