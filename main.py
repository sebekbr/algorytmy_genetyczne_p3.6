# Sebastian Brodziak - algorytmy genetyczne
# TODO - sprawdz czy masz trafienie ( <0.5)
# TODO - usuń najgorszych
# TODO - krzyżuj
# TODO - mutuj
# TODO - ew. dodaj nowych (jak usunąłeś wcześniej)
# TODO - wylicz dodatkowe jak brakuje

import random
import numpy as np

# populacja
population = np.array([
    [1, 2, -1, 3, -4, -1, -2, 2],
    [-3, -1, 2, -3, 4, -5, -2, -1],
    [1, -3, 9, 2, -8, 3, -2, 7],
    [2, -1, 6, 2, 3, 6, -9, -1],
    [3, 1, 4, -5, -5, 1, 3, -4],
    [2, -2, 2, 2, 4, -9, -2, 4],
    [4, 5, 8, -1, -6, 2, 2, -5],
    [-2, 2, 1, 6, 1, -4, -5, 2]])

br = np.array([10, 2, -5, 3, 6, -2, -4, 9])

matrix = np.array([[2, -5, 3, 2, 5, 9, -10, 1],
    [-6, 4, -4, -4, -1, 10, 1, -2],
    [-5, -6, -8, -9, 2, 2, 7, 10],
    [7, -5, -2, -4, -4, 7, 1, -1],
    [8, -10, 1, -9, 5, -7, 0, 9],
    [-3, -9, 5, 10, 2, 2, -9, -5],
    [-8, -3, 10, 2, 3, 7, -9, 1],
    [9, 7, -9, 1, 5, -6, -4, 5],
    [3, 10, 1, 4, 9, 5, -6, 1],
    [-9, 6, 8, 4, -10, 4, -3, 4],
    [7, -3, -5, 3, 9, 8, 0, 3],
    [-3, 0, 10, -2, -1, -8, 9, 8],
    [4, -1, 2, 0, -6, 6, -6, 3],
    [9, 3, 6, 6, 4, -4, 10, -1],
    [8, 8, 10, -3, -4, 0, -10, -5],
    [-8, 0, 10, 5, 2, 1, -3, -7],
    [5, -4, 9, -6, 0, -5, -9, -9],
    [6, -6, 0, 1, -1, 5, -9, 7],
    [-10, -2, -6, -9, 8, -9, 5, -6],
    [0, -5, 0, 2, 5, 9, -10, 1]])

# obliczanie wsp_dos i wpisywanie do macierzy
wsp_dos = []
for i in range(len(matrix)):
    test = np.multiply(matrix[i], population)
    b = np.sum(test, axis=1) # sumowanie wiersza
    wsp_dos.append(sum(abs(b - br)))

# sortowanie
sorted_matrix = np.array([x for _, x in sorted(zip(wsp_dos,matrix))])

# krzyżowanie
# punkt krzyżowania
index = int(len(matrix[0])/2)
