import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.rand(50)
y1 = -x1 + np.random.normal(0, 0.05, 50)

x2 = np.random.rand(50) + 1.5
y2 = -x2 + np.random.normal(0, 0.05, 50) + 3

x = np.concatenate([x1, x2])
y = np.concatenate([y1, y2])

x_outliers = np.array([0.2, 2.5])
y_outliers = np.array([2.5, -1])

x = np.concatenate([x, x_outliers])
y = np.concatenate([y, y_outliers])

plt.figure()
plt.scatter(x, y)

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot with Clusters, Negative Correlation & Outliers')

plt.show()