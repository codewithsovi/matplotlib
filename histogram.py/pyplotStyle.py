import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 1000, 15
x = mu + sigma * np.random.randn(10000)
x.shape #membuat array 1 dimensi

plt.hist(x, bins=50, facecolor='g', alpha=0.75)
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.title('histogram')

plt.text(1020, 500, r'$\mu=1000,\ \sigma=15$')
plt.grid()
plt.show()