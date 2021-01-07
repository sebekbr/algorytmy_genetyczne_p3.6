# Sebastian Brodziak - algorytmy genetyczne
# TODO - sprawdz czy masz trafienie ( <0.5)
# TODO - usuń najgorszych
# TODO - ew. dodaj nowych (jak usunąłeś wcześniej)
# TODO - wylicz dodatkowe jak brakuje
import numpy as np
import random as rand
import os
import time
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
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

br = np.array([10, 2, -5, 3, 6, -2, -4, 9])

equation_param = [-10, 10, 8, 8]


# Populacja z wartościami losowymi
# equation_param = np.random.randint(-10, 10, size=(8, 8))


def gen_population(a, b, c, d):
    return np.random.randint(a, b, size=(c, d))


# Macierz z wartościami losowymi
# matrix = np.random.randint(-10, 10, size=(20, 8))


# obliczanie wsp_dos i wpisywanie do macierzy
def wsp_dost(population):
    wsp_dos = []
    for i in range(len(population)):
        # Mnożenie
        test = np.multiply(population[i], constant_equation)
        # sumowanie wiersza
        b = np.sum(test, axis=1)
        wsp_dos.append(sum(abs(b - br)))
    return np.array(wsp_dos)

# sortowanie
def sorting_population():
    return np.array([y for x, y in sorted(zip(wsp_dost(), constant_population))])


# USUWANIE NAJGORSZYCH
def del_individual_from_pop(del_individual_quantity, sorted_population):
    del_population = np.delete(sorted_population, np.s_[len(sorted_population)-del_individual_quantity:], axis=0)
    return del_population
    # return sorted_population[:-del_individual_quantity]


# KRZYŻOWANIE
def cross(sorted_population):
    # punkt krzyżowania
    cross_point = int(len(constant_population[0]) / 2)
    # crossed = []

    for index in range(0, len(sorted_population) - 1, 2):
        np.append(sorted_population[index][:cross_point], sorted_population[index + 1][cross_point:])
        np.append(sorted_population[index + 1][:cross_point], sorted_population[index][cross_point:])
    return sorted_population

# print(cross(sorting_population()))

# MUTACJA
def mutation(loop_count, crossed_array):
    for loop in range(loop_count):
        random_index = rand.randint(0, len(crossed_array[0])-1)
        random_index2 = rand.randint(0, len(crossed_array[0])-1)
        random_value = rand.randint(-10, 10)

        # Podmiana wartości
        crossed_array[random_index][random_index2] = random_value
        # return muted_array
    return crossed_array

# Dodawnie nowych osobników do populacji
def replacing_last_gens(new_population):
    # new_population = del_individual_from_pop(2)
    temp = np.empty((2, 8), dtype=int) # pusta macierz
    for i in range(2): # generowanie 2 nowych osobników
        temp[i-1] = gen_population(equation_param[0], equation_param[1], 1, equation_param[3])
    arr = np.append(new_population,temp, axis=0) # dodanie osobników do populacji
    return arr


# # Nowe współczynniki
# def new_wsp_dos(arr):
#     new_wsp_dost = []
#
#     for i in range(len(arr)):
#         test2 = np.multiply(arr[i], constant_equation)
#         # sumowanie wiersza
#         b = np.sum(test2, axis=1)
#         new_wsp_dost.append(sum(abs(b - br)))
#     return new_wsp_dost

print("oryginalne wspołczynniki")
print(wsp_dost())
print("Nowe")
print(new_wsp_dos(replacing_last_gens(del_individual_from_pop(2, sorted_population))))
# print("Nowe współczynniki: ")
# print(new_wsp_dos(replacing_last_gens()))

# ---=== WŁAŚCIWY PROGRAM ===---
# print("Aktualna posortowana populacja:")
# print(sorting_population())
#
# print("\nPopulacja po usunięciu dwóch ostatnich:")
# print(del_individual_from_pop(2))
#
# print("\nPo dodaniu dwóch nowych:")
# print(replacing_last_gens())


# print("\nPosortowane:")
# print(np.array([y for x, y in sorted(zip(new_wsp_dost, new_population))]))

# Usuwasz 2 to zostaje 18x8. Potem krzyżujesz, mutujesz i dodajesz dwóch.

# print("Mnożenie z numpy")
# print(wsp_dost())
#
# print("Zwykłe mnożenie:")
#
# for i in range(len(constant_population)):
#     for j in range(len(constant_equation)):
#         test = constant_population[i][j] * constant_equation
#