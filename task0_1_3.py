import numpy as np

SIZE = 5

a = np.floor(10*np.random.random((SIZE, SIZE)))
diag = np.diag(a)

print(a)
print("Matrix trace: ", a.trace())

num = np.size(diag.nonzero())

print("Number of nonzero elements: ", num)
