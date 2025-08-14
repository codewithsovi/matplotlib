import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 4, 5]
y =[2, 4, 5, 5]

plt.scatter(x, y, label='data', color='r')

plt.legend()
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.title('scatter sederhana')

plt.grid()
plt.show()