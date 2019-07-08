import numpy as np
import matplotlib.pyplot as plt

input_array = np.linspace(0, 2 * np.pi, 1000)

sin_curve = np.cos(input_array)
x = input_array
y = x
f,ax = plt.subplots(figsize = (8,5))
ax.plot(x, y, c = '#99badd')
plt.show()
