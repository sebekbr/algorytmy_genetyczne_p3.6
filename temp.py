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
#         score_card.append(population[j])
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


# def crossover(a, b, index):
#     return b[:index] + a[index:], a[:index] + b[index:]
#
#
# def test_crossover():
#     a = sorted_matrix
#     b = sorted_matrix
#     population = [a, b]
#     population += crossover(a, b, index)
#     return population
#
#
# print(test_crossover())


def crossover():
    global parents

    cross_point = int(len(matrix[0])/2)
    parents = parents + tuple([(parents[0][0:cross_point + 1] + parents[1][cross_point + 1:6])])
    parents = parents + tuple([(parents[1][0:cross_point + 1] + parents[0][cross_point + 1:6])])

    print(parents)


# def first_half():
#     for i in range(len(matrix)):
#         print(matrix[i][:cross_point])
#
#
# def second_half():
#     for i in range(len(matrix)):
#         print(matrix[i][cross_point:])