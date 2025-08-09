import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0, 5.0, 50)
x2 = np.linspace(0.0, 2.0, 50)

y1 = np.cos(2* np.pi * x1)
y2 = np.cos(2* np.pi * x2)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Multiple axes dengan oostyle')

ax1.plot(x1, y1, 'r--')
ax1.set_ylabel('nilai cos (x1)')

ax2.plot(x2, y2, 'g--')
ax2.set_ylabel('nilai cos (x2)')

ax2.set_xlabel('nilai x')
plt.show()