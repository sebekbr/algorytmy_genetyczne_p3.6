# Sebastian Brodziak - algorytmy genetyczne
# TODO - sprawdz czy masz trafienie ( <0.5)
# TODO - usuń najgorszych
# TODO - ew. dodaj nowych (jak usunąłeś wcześniej)
# TODO - wylicz dodatkowe jak brakuje

import numpy as np
import random as rand

# Populacja z wartościami losowymi
# population = np.random.randint(-10, 10, size=(8, 8))
def gen_population(a, b, c, d):
    return np.random.randint(a, b, size=(c, d))

br = np.array([10, 2, -5, 3, 6, -2, -4, 9])

population = [-10, 10, 8, 8]

# Macierz z wartościami losowymi
matrix = np.random.randint(-10, 10, size=(20, 8))


# obliczanie wsp_dos i wpisywanie do macierzy
def wsp_dost():
    wsp_dos = []
    for i in range(len(matrix)):
        # Mnożenie
        test = np.multiply(matrix[i], gen_population(population[0], population[1], population[2], population[3]))
        # sumowanie wiersza
        b = np.sum(test, axis=1)
        wsp_dos.append(sum(abs(b - br)))
    return np.array(wsp_dos)

sorted_matrix = np.array([y for x, y in sorted(zip(wsp_dost(), matrix))])


# USUWANIE NAJGORSZYCH
def del_individual_from_pop(del_individual_quantity):
    return sorted_matrix[:-del_individual_quantity]


# KRZYŻOWANIE
def cross():
    # punkt krzyżowania
    cross_point = int(len(matrix[0])/2)

    crossed = []
    for i in range(0, len(sorted_matrix)-1, 2):
        crossed.append(np.append(sorted_matrix[i][:cross_point], sorted_matrix[i+1][cross_point:]))
        crossed.append(np.append(sorted_matrix[i+1][:cross_point], sorted_matrix[i][cross_point:]))
    return np.array(crossed)


crossed_array = cross()

# print(cross())


# MUTACJA
def mutation(loop_count):
    for i in range(loop_count):
        random_index = rand.randint(0, len(crossed_array[0])-1)
        random_index2 = rand.randint(0, len(crossed_array[0])-1)
        random_value = rand.randint(-10, 10)

        # Podmiana wartości
        crossed_array[random_index][random_index2] = random_value
        # return muted_array
    return crossed_array


# print(mutation(4))
np.random.randint(-10, 10, size=(1, 8))
