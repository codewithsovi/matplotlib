import matplotlib.pyplot as plt
import numpy as np

data1 = [25, 85, 40, 50, 30]
data2 =[40, 35, 20, 66, 10]
kat = ['A', 'B', 'C', 'D', 'E']

plt.bar(kat, data1, label='data 1')
plt.bar(kat, data2, label='data 2', bottom=data1)

plt.legend()

plt.grid(linestyle='--', linewidth=1, axis='y', alpha=0.75)
plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.title('bar plot')

plt.show()