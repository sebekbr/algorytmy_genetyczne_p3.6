# Sebastian Brodziak - algorytmy genetyczne v0.2
import random

# populacja
population = [[1, 2, -1, 3, -4, -1, -2, 2],
              [-3, -1, 2, -3, 4, -5, -2, -1],
              [1, -3, 9, 2, -8, 3, -2, 7],
              [2, -1, 6, 2, 3, 6, -9, -1],
              [3, 1, 4, -5, -5, 1, 3, -4],
              [2, -2, 2, 2, 4, -9, -2, 4],
              [4, 5, 8, -1, -6, 2, 2, -5],
              [-2, 2, 1, 6, 1, -4, -5, 2]]

a = [2, -5, 3, 2, 5, 9, -10, 1]

# Obliczanie b
b = []
for subl in population:
    temp = []
    for i in range(len(subl)):
        temp.append(subl[i] * a[i])
    b.append(sum(temp))

print('Wartość b:\n', b)

br = [10, 2, -5, 3, 6, -2, -4, 9]

b_minus_br = []
for i in range(8):
    b_minus_br.append(abs(b[i] - br[i]))

print('Wartosc abs(b-br):\n', sum(b_minus_br))

# macierz współczynników losowych a o wymiarze 20x8

