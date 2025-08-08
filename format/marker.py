import matplotlib.pyplot as plt
import numpy as np

# marker = style untuk plotnya
"""
- garis, . dot, * bintang, -- garis putus2,
s square kotak, caping
"""

plt.plot([1, 2, 3, 4, 5], [2, 4, 5, 5, 7], 'b-')
# pemetaan axis
plt.axis([0, 6, 0, 20])
plt.grid()
plt.show()