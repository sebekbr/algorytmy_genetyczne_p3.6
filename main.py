# Sebastian Brodziak - algorytmy genetyczne v0.2
import random
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

# populacja
population = [[1, 2, -1, 3, -4, -1, -2, 2], [-3, -1, 2, -3, 4, -5, -2, -1], [1, -3, 9, 2, -8, 3, -2, 7],
              [2, -1, 6, 2, 3, 6, -9, -1], [3, 1, 4, -5, -5, 1, 3, -4], [2, -2, 2, 2, 4, -9, -2, 4],
              [4, 5, 8, -1, -6, 2, 2, -5], [-2, 2, 1, 6, 1, -4, -5, 2]]
fitness_score = [10, 2, -5, 3, 6, -2, -4, 9]
total_fitness = sum([10, 2, -5, 3, 6, -2, -4, 9])

score_card = []
# grupowanie wyników z osobnikami populacji
for i in range(8):
    for j in range(8):
        score_card.append(fitness_score[j])
        score_card.append(population[j])

# miejsce podziału genomu
crossover_point = 4
