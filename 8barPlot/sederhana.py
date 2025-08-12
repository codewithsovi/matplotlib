import matplotlib.pyplot as plt
import numpy as np

data =[25, 45, 55, 125, 225]
kategori = ['A', 'B', 'C', 'D', 'E']

plt.bar(kategori, data, color='red', alpha=0.75)
plt.grid(linestyle='--', linewidth='1', axis='y', alpha=0.25)

plt.xlabel('kategori')
plt.ylabel('data')
plt.title('bar plot')

plt.show()