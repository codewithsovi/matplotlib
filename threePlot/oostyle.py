import matplotlib.pyplot as plt
import numpy as np

# linspace (start, stop, step)
x = np.linspace(0, 5, 20)

fig, ax = plt.subplots()

ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label='cubig')

ax.legend()
ax.set_xlabel('sumbu x')
ax.set_ylabel('sumbu y')
ax.set_title('3 plot')
plt.show()