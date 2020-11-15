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


# sortowanie
# def sort():
#     sorted_matrix = []
#     for _, x in sorted(zip(wsp_dos,matrix)):
#         sorted_matrix.append(np.array(x))