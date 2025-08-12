import matplotlib.pyplot as plt
import numpy as np

kat = ['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 225]
color = ['pink', 'cyan', 'blue', '#eD3364', 'yellowgreen', 'skyblue']
# explode in digunakan untuk menarik beberapa bagian dari pie(irisan pie) default=0.
explode_var = [0., 0., 0.2, 0., 0.08 ]

plt.pie(data, labels=kat, autopct='%1.1f', colors=color, explode=explode_var, startangle=90)

plt.legend()
plt.title('pie plot')
plt.show()