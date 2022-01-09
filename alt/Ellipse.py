import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(-10,10,1000)
a=1
b=2
y=np.sqrt(1-(x/a)**2)*b**2
plt.plot(x,y)
plt.plot(x,-y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('graph of hyperbola')
plt.grid(True)
plt.show()