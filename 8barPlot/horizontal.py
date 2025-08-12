import matplotlib.pyplot as plt
import numpy as np

data =[25, 45, 55, 125, 225]
kategori = ['A', 'B', 'C', 'D', 'E']

#1. terkecil - terbesar
plt.barh(kategori, data, color='blue', alpha=0.75)

#2. terbesar - terkecil
# plt.barh(kategori[:-1], data[:-1])

plt.show()