import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y = x + np.random.normal(size=50)

plt.plot(x, y, 'o')
b = (np.mean(x * y) - np.mean(x)*np.mean(y))/(np.mean(x*x)-np.mean(x)**2)
a = np.mean(y) - b*np.mean(x)
plt.plot(x, x * b + a, '-')

plt.errorbar(x, y, yerr=1, xerr=0.5)


plt.show()
