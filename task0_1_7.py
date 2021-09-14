import numpy as np

n, m = 3, 4

A = np.array(np.floor(10*np.random.random((n, m))))
B = np.array(np.floor(10*np.random.random((n, m))))

C = np.dot(A.T, B)

print(A)
print(B)

print(C)
