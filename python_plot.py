import numpy as np
import matplotlib.pyplot as plt

input_array = np.linspace(0, 2 * np.pi, 1000)

sin_curve = np.cos(input_array)

f,ax = plt.subplots(figsize = (8,5))
ax.plot(input_array, sin_curve, c = '#99badd')
plt.show()
