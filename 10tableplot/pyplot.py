import matplotlib.pyplot as plt
import numpy as np

data = [['sovi', 30], ['dea', 50], ['kurnia', 100]]

table = plt.table(cellText=data, loc='center', colLabels=['nama', 'nilai'])
table.set_fontsize(14)
table.scale(1,4)
plt.gca().axis('off') 

plt.show()