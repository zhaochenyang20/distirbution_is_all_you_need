import random
import numpy as np
from matplotlib import pyplot as plt

n_experiment = 100
p = [0.2, 0.3, 0.5]
x = np.arange(n_experiment)
y = []

def categorical(p, k):
    if k <= n_experiment * p[0]:
        return p[0]
    elif k <= n_experiment * (p[0] + p[1]):
        return p[1]
    else:
        return p[2]


for _ in range(n_experiment):
    pick = categorical(p, k=random.randint(0, 100))
    y.append(pick)

u, s = np.mean(y), np.std(y)
plt.scatter(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))
plt.legend()
plt.show()