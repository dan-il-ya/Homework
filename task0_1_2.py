import numpy as np

SIZE = 4

a = np.floor(SIZE*np.random.random(SIZE)).astype(int)
b = np.floor(SIZE*np.random.random(SIZE)).astype(int)
print(a, '\n', b)
M = np.array(np.floor(10*np.random.random((SIZE, SIZE))))

print(M)
print(M[a, b])