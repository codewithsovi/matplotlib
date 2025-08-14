import matplotlib.pyplot as plt
import numpy as np

data=[['sovi', 30], ['dani', 21], ['leli', 50]]
fig, ax = plt.subplots()

table = plt.table(cellText=data, colLabels=['Nama', 'Usia'], loc='center')
table.set_fontsize(14)
table.scale(1,4)

ax.axis('off')
plt.title('table')

plt.show()