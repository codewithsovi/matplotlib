import matplotlib.pyplot as plt
import numpy as np

# arange(start, stop, interval )
# interval = banyaknya data
x = np.arange(0., 5., 0.2)

plt.plot(x, x , label='linear')
plt.plot(x, x**2 , label='kuadrat')
plt.plot(x, x**3 , label='kubik')

plt.xlabel('sumbu x')
plt.ylabel('sumbu y')
plt.title('pyplot style')

plt.grid()
plt.legend()
plt.show()