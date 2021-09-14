import numpy as np

(width_a, width_b, high) = 1 + np.abs(np.floor(10*np.random.random((3))))
(width_a, width_b, high) = (int(width_a), int(width_b), int(high))
a = np.floor(10*np.random.random((high, width_a)))
b = np.floor(10*np.random.random((high, width_b)))

c = np.hstack((a, b))

print(a)
print(b)
print(c)
