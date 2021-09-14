import numpy as np

SIZE = 4

A = np.array(np.floor(10*np.random.random((SIZE, SIZE))))

A = A - np.mean(A, axis=0)

M = np.sqrt(np.diag(np.dot(A.T, A)))

A[M > 0] /= M
print(A)
