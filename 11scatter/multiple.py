import matplotlib.pyplot as plt
import numpy as np

x1 =[1, 2, 3, 4, 5]
y1 =[3, 4, 5, 6, 3]

x2=[2, 4, 5, 6, 8]
y2 = [3, 9, 7, 1, 3]

# edgecolors itu garis dimarkernya bisa sih ngatur markernya
plt.scatter(x1, y1, label='data 1', color='green', linewidths=1, edgecolors='red', s=100)
plt.scatter(x2, y2, label='data 2', color='blue', linewidths=1, edgecolors='yellow', s=100)

plt.legend()

plt.xlabel('x')
plt.ylabel('y')

plt.show()