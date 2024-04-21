import numpy as np

x = np.array([1.2, 2.0, 2.8, 3.6, 4.2, 5.0])
y = np.array([2.5, 3.6, 4.1, 5.0, 5.9, 6.3])
X = np.vstack([x, np.ones(len(x))]).T
b1, b0 = np.linalg.lstsq(X, y, rcond=None)[0]

print(f"Slope (b1): {b1:.4f}")
print(f"Intercept (b0): {b0:.4f}")
