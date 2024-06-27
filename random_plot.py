from matplotlib import pyplot as plt
import random
import numpy as np

x = np.arange(0, 100, 2)
y = np.array([random.randint(0,100) for _ in range(50)])
y = np.random.randint(0, 100, 50)

plt.plot(x, y)
plt.title('Random plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('out/random_plot.png')