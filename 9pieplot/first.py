import matplotlib.pyplot as plt
import numpy as np

kat =['A', 'B', 'C', 'D', 'E']
data = [215, 130, 245, 210, 225]

plt.pie(data, labels=kat, autopct='%1.1f', startangle=90)
plt.title('pie plot')
plt.show()