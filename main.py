# Sebastian Brodziak - algorytmy genetyczne
import numpy as np
import random as rand
import wsp_dost
import cross
import mutation
# wylicz wspolczynniki dostosowania
# posortuj wg wspolczynnika
# TODO - sprawdz czy masz trafienie ( <0.5)
# TODO - usuń najgorszych
# krzyzuj
# mutuj
# TODO - ew. dodaj nowych (jak usunąłeś wcześniej)
# TODO - wylicz dodatkowe jak brakuje


# Populacja z wartościami losowymi
population = np.random.randint(-10, 10, size=(8, 8))

br = np.array([10, 2, -5, 3, 6, -2, -4, 9])

# Macierz z wartościami losowymi
matrix = np.random.randint(-10, 10, size=(20, 8))

wsp_dost()
# print("----------------------------------")

sorted_matrix = np.array([y for x, y in sorted(zip(wsp_dost(), matrix))])

# KRZYŻOWANIE
crossed_array = cross()
print(cross())


# MUTACJA
print(mutation(4))