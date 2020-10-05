#Sebastian Brodziak - algorytmy genetyczne v0.1
import numpy as np
A = np.array([[1,2,-1,3,-4,-1,-2,2],
             [-3,-1,2,-3,4,-5,-2,-1],
             [1,-3,9,2,-8,3,-2,7],
             [2,-1,6,2,3,6,-9,-1],
             [3,1,4,-5,-5,1,3,-4],
             [2,-2,2,2,4,-9,-2,4],
             [4,5,8,-1,-6,2,2,-5],
             [-2,2,1,6,1,-4,-5,2]])

B = np.array([10,2,-5,3,6,-2,-4,9])

print('matrix A\n', A)

print(np.linalg.det(A))

rownanie = 1*a + 2*b + -1*c