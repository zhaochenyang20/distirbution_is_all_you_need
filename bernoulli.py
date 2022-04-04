import random
import numpy as np
from matplotlib import pyplot as plt

n_experiment = 30
p = 0.8

def bernoulli(p, k):
    return p if k <= n_experiment * p else 1 - p

x = np.arange(n_experiment)
y = []
for _ in range(n_experiment):
    pick = bernoulli(p, k=random.randint(0, n_experiment + 1))
    y.append(pick)

u, s = np.mean(y), np.std(y)
plt.scatter(x, y, label=r'$\mu=%.2f,\ \sigma=%.2f$' % (u, s))
plt.legend()
plt.show()