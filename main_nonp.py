# Sebastian Brodziak - algorytmy genetyczne
# TODO - sprawdz czy masz trafienie ( <0.5)
# TODO - usuń najgorszych
# TODO - ew. dodaj nowych (jak usunąłeś wcześniej)
# TODO - wylicz dodatkowe jak brakuje

import numpy as np
import random as rand

# # równanie
constant_equation = [
    [1, 2, -1, 3, -4, -1, -2, 2],
    [-3, -1, 2, -3, 4, -5, -2, -1],
    [1, -3, 9, 2, -8, 3, -2, 7],
    [2, -1, 6, 2, 3, 6, -9, -1],
    [3, 1, 4, -5, -5, 1, 3, -4],
    [2, -2, 2, 2, 4, -9, -2, 4],
    [4, 5, 8, -1, -6, 2, 2, -5],
    [-2, 2, 1, 6, 1, -4, -5, 2]]

# # Stała macierz populacji
constant_population = [[2, -5, 3, 2, 5, 9, -10, 1],
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
                       [0, -5, 0, 2, 5, 9, -10, 1]]

br = [10, 2, -5, 3, 6, -2, -4, 9]

equation_param = [-10, 10, 8, 8]


# Populacja z wartościami losowymi
def gen_population(min_range, max_range, row, col):
    return [[rand.randrange(min_range, max_range) for i in range(col)] for i in range(row)]

# print(gen_population(-10, 10, 1, 8))


# Macierz z wartościami losowymi
# matrix = np.random.randint(-10, 10, size=(20, 8))


# obliczanie wsp_dos i wpisywanie do macierzy
def wsp_dost_np():
    wsp_dos = []
    for i in range(len(constant_population)):
        # Mnożenie
        test = np.multiply(constant_population[i], constant_equation)
        # sumowanie wiersza
        b = np.sum(test, axis=1)
        wsp_dos.append(sum(abs(b - br)))
    return np.array(wsp_dos)
print("Z numpy:")
print(wsp_dost_np())

def wsp_dost():
    wsp_dos = []
    temp = []
    for i in range(len(constant_population)):
        for j in range(len(constant_equation)):
            row_index_multiply = constant_population[i][j] * constant_equation[i][j]
            temp.append(row_index_multiply)
        int(b = sum(temp))
        # sumowanie wiersza
        # b = np.sum(test, axis=1)
        wsp_dos.append(sum(abs(b - br)))
    return np.array(wsp_dos)
print("Bez numpy:")
print(wsp_dost())

# # sortowanie
def sorting_population():
    sorted_population = [y for x, y in sorted(zip(wsp_dost(), constant_population))]
    return sorted_population


# # USUWANIE NAJGORSZYCH
# def del_individual_from_pop(del_individual_quantity):
#     del_population = np.delete(sorted_population, np.s_[len(sorted_population)-del_individual_quantity:], axis=0)
#     return del_population
#     # return sorted_population[:-del_individual_quantity]
#
# # KRZYŻOWANIE
# def cross():
#     # punkt krzyżowania
#     cross_point = int(len(constant_population[0]) / 2)
#
#     crossed = []
#
#     for i in range(0, len(sorted_population) - 1, 2):
#         crossed.append(np.append(sorted_population[i][:cross_point], sorted_population[i + 1][cross_point:]))
#         crossed.append(np.append(sorted_population[i + 1][:cross_point], sorted_population[i][cross_point:]))
#     return np.array(crossed)
#
#
# # MUTACJA
# def mutation(loop_count):
#     crossed_array = cross()
#     for i in range(loop_count):
#         random_index = rand.randint(0, len(crossed_array[0])-1)
#         random_index2 = rand.randint(0, len(crossed_array[0])-1)
#         random_value = rand.randint(-10, 10)
#
#         # Podmiana wartości
#         crossed_array[random_index][random_index2] = random_value
#         # return muted_array
#     return crossed_array
#
#
# # ---=== WŁAŚCIWY PROGRAM ===---
#
# # gen_population(equation_param[0], equation_param[1], equation_param[2], equation_param[3])
# print("Aktualna posortowana populacja:")
# print(sorted_population)
#
# print("\nPopulacja po usunięciu dwóch ostatnich:")
# # print(del_individual_from_pop(2))
#
# print("\nPo dodaniu dwóch nowych:")
# def replacing_last_gens():
#     new_population = del_individual_from_pop(2)
#     for row in range(1, 2):
#         new_value = gen_population(equation_param[0], equation_param[1], 1, equation_param[3])
#         new_population = np.append(new_population, new_value, axis=0)
#     return new_population
#     # sorted_population.append(gen_population(equation_param[0], equation_param[1], 1, equation_param[3]))
#
# print(replacing_last_gens())
#
# # Nowe współczynniki
# new_wsp_dost = []
# for i in range(len(constant_population)):
#     test2 = np.multiply(constant_population[i], constant_equation)
#     # sumowanie wiersza
#     b = np.sum(test2, axis=1)
#     new_wsp_dost.append(sum(abs(b - br)))
#
#
# # print("\nPosortowane:")
# # print(np.array([y for x, y in sorted(zip(new_wsp_dost, new_population))]))
#
# # 20x8 to 20 osobników po 8 genów
# # Usuwasz 2 to zostaje 18x8. Potem krzyżujesz, mutujesz i dodajesz dwóch.
#
# # print("Mnożenie z numpy")
# # print(wsp_dost())
# #
# # print("Zwykłe mnożenie:")
# #
# # for i in range(len(constant_population)):
# #     for j in range(len(constant_equation)):
# #         test = constant_population[i][j] * constant_equation
# #