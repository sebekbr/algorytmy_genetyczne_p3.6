# Od uruchomienia programu to idzie jakoś tak:
# generowanie populacji
# * wyliczenie współczynników dostosowania
# sortowanie
# sprawdzenie końca algorytmu
# usuwanie najgorszych
# krzyżowanie
# mutowanie
# dodanie nowych (w miejsce usuniętych)
# powrót do *



# równanie
# a, b, c, d, e, f, g, h, x0, x1, x2, x3, x4, x5, x6, x7 = 0
# eq = a*x0 + b*x1 + c*x2 + d*x3 + e*x4 + f*x5 + g*x6 + h*x7

# generowanie liczb losowych
# a = []
# x = []
#
# for i in range(8):
#     a.append(random.randint(-10, 10))
#     x.append(random.randint(-10, 10))
# print(a)
# print(x)

# Mnożenie a*x
# multi = []
# for i in range(8):
#     multi.append(a[i]*x[i])
#
# print(multi)

# grupowanie wyników z osobnikami populacji
# score_card = []
# for i in range(8):
#     for j in range(8):
#         score_card.append(constant_equation[j])
#         score_card.append(br[j])
#
# # miejsce podziału genomu
# crossover_point = 4
# print('Wartosc score_card:\n', score_card)

# Obliczanie b
b = []
for subl in population:
    temp = []
    for i in range(len(subl)):
        temp.append(subl[i] * a[i])
    b.append(sum(temp))

print('Wartość b:\n', b)



b_minus_br = []
for i in range(8):
    b_minus_br.append(abs(b[i] - br[i]))

print('Wartosc abs(b-br):\n', sum(b_minus_br))


# sortowanie
# def sort():
#     sorted_population = []
#     for _, x in sorted(zip(wsp_dos,matrix)):
#         sorted_population.append(np.array(x))


# Usuwanie
# muted_array = np.delete(crossed_array[19], random_index2)

# Wstawianie
# muted_array = np.insert(muted_array, random_index2, random_value)

# # populacja
# constant_equation = np.array([
#     [1, 2, -1, 3, -4, -1, -2, 2],
#     [-3, -1, 2, -3, 4, -5, -2, -1],
#     [1, -3, 9, 2, -8, 3, -2, 7],
#     [2, -1, 6, 2, 3, 6, -9, -1],
#     [3, 1, 4, -5, -5, 1, 3, -4],
#     [2, -2, 2, 2, 4, -9, -2, 4],
#     [4, 5, 8, -1, -6, 2, 2, -5],
#     [-2, 2, 1, 6, 1, -4, -5, 2]])


# # Stała macierz
# constant_population = np.array([[2, -5, 3, 2, 5, 9, -10, 1],
#                    [-6, 4, -4, -4, -1, 10, 1, -2],
#                    [-5, -6, -8, -9, 2, 2, 7, 10],
#                    [7, -5, -2, -4, -4, 7, 1, -1],
#                    [8, -10, 1, -9, 5, -7, 0, 9],
#                    [-3, -9, 5, 10, 2, 2, -9, -5],
#                    [-8, -3, 10, 2, 3, 7, -9, 1],
#                    [9, 7, -9, 1, 5, -6, -4, 5],
#                    [3, 10, 1, 4, 9, 5, -6, 1],
#                    [-9, 6, 8, 4, -10, 4, -3, 4],
#                    [7, -3, -5, 3, 9, 8, 0, 3],
#                    [-3, 0, 10, -2, -1, -8, 9, 8],
#                    [4, -1, 2, 0, -6, 6, -6, 3],
#                    [9, 3, 6, 6, 4, -4, 10, -1],
#                    [8, 8, 10, -3, -4, 0, -10, -5],
#                    [-8, 0, 10, 5, 2, 1, -3, -7],
#                    [5, -4, 9, -6, 0, -5, -9, -9],
#                    [6, -6, 0, 1, -1, 5, -9, 7],
#                    [-10, -2, -6, -9, 8, -9, 5, -6],
#                    [0, -5, 0, 2, 5, 9, -10, 1]])


# sorted_matrix_no_worst = np.delete(sorted_population, len(sorted_population)-1)
