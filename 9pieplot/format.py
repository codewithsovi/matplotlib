import matplotlib.pyplot as plt
import numpy as np

kat = ['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 225]
color = ['pink', 'cyan', 'blue', '#eD3364', 'yellowgreen', 'skyblue']

plt.pie(data, labels=kat, autopct='%1.1f', colors=color, startangle=90)
plt.legend()
plt.title('pie plot')
plt.show()