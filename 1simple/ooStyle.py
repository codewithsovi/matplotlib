import matplotlib.pyplot as plt
import numpy

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# OOStyle
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('sumbu x')
ax.set_ylabel('sumbu y')
ax.set_title('percobaan pertama')
plt.show()