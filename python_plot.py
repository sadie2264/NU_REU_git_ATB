import numpy as np
import matplotlib.pyplot as plt

input_array = np.linspace(0, 2 * np.pi, 1000)


exp_plot =np.exp(input_array)


sin_curve = np.cos(input_array)
x = input_array
f,ax = plt.subplots(figsize = (8,5))
ax.plot(x, y, c = '#99badd')
plt.show()
