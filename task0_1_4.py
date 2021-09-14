import numpy as np

T = np.round(100*np.random.random((2, 3, 4, 5))).astype(int)
F = T.flatten()

print(T)
print(np.array(np.unique(F, return_counts=True)))
