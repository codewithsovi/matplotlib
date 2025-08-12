import matplotlib.pyplot as plt
import numpy as np

data1 = [25, 85, 40, 50, 30]
data2 =[40, 35, 20, 66, 10]
kat = ['A', 'B', 'C', 'D', 'E']
x= np.arange(len(kat))

width = 0.35

plt.bar(x-width/2, data1, width, label='data 1')
plt.bar(x-width/2, data2, width, label='data 2')

plt.xticks(x, kat)

plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.25)

plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.title('bar plot')

plt.legend()
plt.show()