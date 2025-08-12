import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 1000, 15
x = mu + sigma * np.random.randn(10000)
x.shape

fig, ax =plt.subplots()

ax.hist(x, bins=50, facecolor='b', alpha=0.75)
ax.set_xlabel('sumbu x')
ax.set_ylabel('sumbu y')
ax.set_title('histogram')

ax.text(1020, 500, r'$\mu=1000,\ \sigma=15$')
ax.grid()
plt.show()