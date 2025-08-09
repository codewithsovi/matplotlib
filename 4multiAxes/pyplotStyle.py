import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0, 5.0, 50)
x2 = np.linspace(0.0, 2.0, 50)

y1 = np.cos(2* np.pi * x1)
y2 = np.cos(2* np.pi * x2)

plt.subplot(2,1,1)
plt.plot(x1, y1, 'r--')
plt.title('2 axes')
plt.ylabel('cos x1')

plt.subplot(2,1,2)
plt.plot(x2, y2, 'b--')
plt.ylabel('cos x2')
plt.xlabel('nilai x')

plt.show()