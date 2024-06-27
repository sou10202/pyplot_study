from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0.0, 10.0, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)', color='gray', linestyle='--', linewidth=2, marker='o', markersize=5)
plt.plot(x, y2, label='cos(x)', color='green', linestyle='-.', linewidth=2, marker='D', markersize=5)
plt.legend()
plt.title("To study custom plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("out/custom_plot.png")