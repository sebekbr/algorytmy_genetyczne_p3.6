# Sebastian Brodziak - algorytmy genetyczne
# TODO - sprawdz czy masz trafienie ( <0.5)
# TODO - usuń najgorszych
# TODO - ew. dodaj nowych (jak usunąłeś wcześniej)
# TODO - wylicz dodatkowe jak brakuje

import numpy as np
import random as rand

# # równanie
constant_equation = np.array([
    [1, 2, -1, 3, -4, -1, -2, 2],
    [-3, -1, 2, -3, 4, -5, -2, -1],
    [1, -3, 9, 2, -8, 3, -2, 7],
    [2, -1, 6, 2, 3, 6, -9, -1],
    [3, 1, 4, -5, -5, 1, 3, -4],
    [2, -2, 2, 2, 4, -9, -2, 4],
    [4, 5, 8, -1, -6, 2, 2, -5],
    [-2, 2, 1, 6, 1, -4, -5, 2]])


# # Stała macierz populacji
constant_population = np.array([[2, -5, 3, 2, 5, 9, -10, 1],
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

# Populacja z wartościami losowymi
# equation_param = np.random.randint(-10, 10, size=(8, 8))


def gen_population(a, b, c, d):
    return np.random.randint(a, b, size=(c, d))


br = np.array([10, 2, -5, 3, 6, -2, -4, 9])

equation_param = [-10, 10, 8, 8]

# Macierz z wartościami losowymi
# matrix = np.random.randint(-10, 10, size=(20, 8))


# obliczanie wsp_dos i wpisywanie do macierzy
def wsp_dost():
    wsp_dos = []
    for i in range(len(constant_population)):
        # Mnożenie
        # test = np.multiply(constant_population[i], gen_population(equation_param[0], equation_param[1],
        #                                                       equation_param[2], equation_param[3]))
        test = np.multiply(constant_population[i], constant_equation)
        # sumowanie wiersza
        b = np.sum(test, axis=1)
        wsp_dos.append(sum(abs(b - br)))
    return np.array(wsp_dos)

# sortowanie
sorted_population = np.array([y for x, y in sorted(zip(wsp_dost(), constant_population))])


# USUWANIE NAJGORSZYCH
def del_individual_from_pop(del_individual_quantity):
    return sorted_population[:-del_individual_quantity]


# KRZYŻOWANIE
def cross():
    # punkt krzyżowania
    cross_point = int(len(constant_population[0]) / 2)

    crossed = []

    for i in range(0, len(sorted_population) - 1, 2):
        crossed.append(np.append(sorted_population[i][:cross_point], sorted_population[i + 1][cross_point:]))
        crossed.append(np.append(sorted_population[i + 1][:cross_point], sorted_population[i][cross_point:]))
    return np.array(crossed)


crossed_array = cross()

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





# ---=== WŁAŚCIWY PROGRAM ===---


# gen_population(equation_param[0], equation_param[1], equation_param[2], equation_param[3])
print("Aktualna posortowana populacja:")
print(sorted_population)

print("\nPopulacja po usunięciu dwóch ostatnich:")
print(del_individual_from_pop(2))

print("\nPo dodaniu dwóch nowych:")
# sorted_population.append(gen_population(equation_param[0], equation_param[1], 1, equation_param[3]))
for row in range(1,2):
    new_population = np.insert(sorted_population, sorted_population[-row:],
                               gen_population(equation_param[0], equation_param[1], 1, equation_param[3]), axis=0)

print(new_population)

# Nowe współczynniki
new_wsp_dost = []
for i in range(len(constant_population)):
    test2 = np.multiply(constant_population[i], constant_equation)
    # sumowanie wiersza
    b = np.sum(test2, axis=1)
    new_wsp_dost.append(sum(abs(b - br)))
np.array(new_wsp_dost)

print("\nPosortowane:")
print(np.array([y for x, y in sorted(zip(new_wsp_dost, new_population))]))

# 20x8 to 20 osobników po 8 genów
# Usuwasz 2 to zostaje 18x8. Potem krzyżujesz, mutujesz i dodajesz dwóch.
# Jak coś to pokaż co zrobiłeś.

