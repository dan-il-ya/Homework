import numpy as np
import matplotlib.pyplot as plt

MATRIX_SIZE = 300
BIN_NUMBER = 30
REPEAT_NUMBER = 50
PLOT_HIST = 0

N = MATRIX_SIZE
M = np.random.normal(size=(N, N))
S = M.T + M
eigs = np.linalg.eig(S)[0]
Y, bins, _ = plt.hist(eigs, BIN_NUMBER, alpha=0.0)
DTST = Y


if PLOT_HIST:
    plt.hist(eigs, bins=bins, alpha=0.5)


for i in range(REPEAT_NUMBER):
    M = np.random.normal(size=[N, N])
    S = M + M.T
    eigs = np.linalg.eig(S)[0]
    DTST = np.vstack([DTST, plt.hist(eigs, bins=bins, alpha=0.0)[0]])
DTST = DTST.T


plt.errorbar(bins[1:], DTST.mean(axis=1), yerr=DTST.std(axis=1), color='r')
plt.show()
