import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 120)
plt.plot(x, np.sin(x)**2 - np.cos(x)**2)
print(5)
plt.show() 