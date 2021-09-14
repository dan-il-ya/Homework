import numpy as np

SIZE = 4

M = np.array(np.floor(10*np.random.random((SIZE, SIZE)))) - 5
N = np.array(np.floor(10*np.random.random((SIZE, SIZE)))) - 5

print(M)
print(N)

N[M < 0] = 0

print(N)
