import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, np.nan, 30, np.nan, 50])

mean_value = np.nanmean(y)
y[np.isnan(y)] = mean_value

plt.plot(x, y, marker='o')
plt.title("Plot After Replacing Missing Values")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()