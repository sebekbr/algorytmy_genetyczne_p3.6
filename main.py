# Sebastian Brodziak - algorytmy genetyczne
# wylicz wspolczynniki dostosowania
# posortuj wg wspolczynnika
# TODO - sprawdz czy masz trafienie ( <0.5)
# TODO - usuń najgorszych
# krzyzuj
# mutuj
# TODO - ew. dodaj nowych (jak usunąłeś wcześniej)
# TODO - wylicz dodatkowe jak brakuje

import numpy as np
import random as rand

# populacja
constant_population = np.array([
    [1, 2, -1, 3, -4, -1, -2, 2],
    [-3, -1, 2, -3, 4, -5, -2, -1],
    [1, -3, 9, 2, -8, 3, -2, 7],
    [2, -1, 6, 2, 3, 6, -9, -1],
    [3, 1, 4, -5, -5, 1, 3, -4],
    [2, -2, 2, 2, 4, -9, -2, 4],
    [4, 5, 8, -1, -6, 2, 2, -5],
    [-2, 2, 1, 6, 1, -4, -5, 2]])

population = np.random.randint(-10, 10, size=(8, 8))

br = np.array([10, 2, -5, 3, 6, -2, -4, 9])

constant_matrix = np.array([[2, -5, 3, 2, 5, 9, -10, 1],
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

matrix = np.random.randint(-10, 10, size=(20, 8))
# print(matrix)
# print("----------------------------------")

# obliczanie wsp_dos i wpisywanie do macierzy
def wsp_dost():
    wsp_dos = []
    for i in range(len(constant_matrix)):
        test = np.multiply(constant_matrix[i], constant_population)
        # sumowanie wiersza
        b = np.sum(test, axis=1)
        wsp_dos.append(sum(abs(b - br)))
    return np.array(wsp_dos)


# print(wsp_dost())
# print("----------------------------------")

sorted_matrix = np.array([y for x, y in sorted(zip(wsp_dost(), constant_matrix))])

# print(sorted_matrix)
# print("----------------------------------")

# punkt krzyżowania
cross_point = int(len(constant_matrix[0]) / 2)

# KRZYŻOWANIE
def cross():
    crossed = []
    for i in range(0, len(sorted_matrix)-1, 2):
        crossed.append(np.append(sorted_matrix[i][:cross_point], sorted_matrix[i+1][cross_point:]))
        crossed.append(np.append(sorted_matrix[i+1][:cross_point], sorted_matrix[i][cross_point:]))
    return np.array(crossed)


print(cross())
print(("--------------------------------"))

# Mutation
def mutation():
    crossed_array = cross()
    random_index = rand.randint(0, len(crossed_array[0])-1)
    random_index2 = rand.randint(0, len(crossed_array[0])-1)
    random_value = rand.randint(-10, 10)

    # Deleting item
    muted_array = np.delete(crossed_array[19], random_index2)

    # Inserting item
    mod_arr = np.insert(muted_array, random_index2, random_value)

    return mod_arr

print(mutation())