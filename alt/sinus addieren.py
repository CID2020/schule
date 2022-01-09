import numpy as np
from matplotlib import pyplot as plt
import math
fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2, sharey=ax1)
ax3 = fig.add_subplot(3, 1, 3, sharey=ax1)
t = np.linspace(0,3,1000)
ax1.plot(t, np.sin(2 * np.pi * t))
ax2.plot(t, np.cos(2 * np.pi * t))
ax3.plot(t, 2*np.cos(2 * np.pi * t))

plt.show()