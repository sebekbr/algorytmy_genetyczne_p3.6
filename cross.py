import numpy as np
from main import sorted_matrix, matrix

# KRZYŻOWANIE

def cross():
    # punkt krzyżowania
    cross_point = int(len(matrix[0]) / 2)

    crossed = []
    for i in range(0, len(sorted_matrix)-1, 2):
        crossed.append(np.append(sorted_matrix[i][:cross_point], sorted_matrix[i+1][cross_point:]))
        crossed.append(np.append(sorted_matrix[i+1][:cross_point], sorted_matrix[i][cross_point:]))
    return np.array(crossed)