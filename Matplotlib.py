# Visualization

# importing libraries
import pandas as pd
import numpy as np
# Created by John Hunter
import matplotlib.pyplot as plt


x = np.linspace(0, 5, 11)
y = x**2

# Basic matplotlib commands
plt.plot(x, y, 'r')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('X versus Y')
plt.show()

# Multiplot on same canvas
# plt.subplot(nrows, ncols, index, **kwargs)
plt.subplot(1,2,1)
plt.plot(x, y, 'r')
plt.subplot(1,2,2)
plt.plot(y, x, 'g')


plt.subplot()
plt.plot(x, x**2, 'r')
# plt.subplot(1,2,2)
plt.plot(x, x**3, 'g')

# Specialized plot types
# Scatter plot
plt.scatter(x, y)

# Histogram


