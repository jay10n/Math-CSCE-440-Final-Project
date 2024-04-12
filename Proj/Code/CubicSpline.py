
import numpy as np


def cubic_spline(x, y):
    n = len(x)
    a = y.copy()
    h = np.diff(x)

    # So tthomas algorithm for tridiagonal matrix.
    # system of equations
    A = np.zeros((n - 2, n - 2))
    b = np.zeros(n - 2)

    for i in range(1, n - 1):
        if i != 1:
            A[i - 1, i - 2] = h[i - 1]
        A[i - 1, i - 1] = 2 * (h[i - 1] + h[i])
        if i != n - 2:
            A[i - 1, i] = h[i]
        b[i - 1] = 3 * ((a[i + 1] - a[i]) / h[i] - (a[i] - a[i - 1]) / h[i - 1])

    #thomas algorithm
    c = np.zeros_like(a)
    c[1:n - 1] = np.linalg.solve(A, b)

    # Step 2: Compute b and d
    b = np.zeros_like(a)
    d = np.zeros_like(a)
    for i in range(1, n):
        b[i - 1] = (a[i] - a[i - 1]) / h[i - 1] - h[i - 1] * (c[i] + 2 * c[i - 1]) / 3
        d[i - 1] = (c[i] - c[i - 1]) / (3 * h[i - 1])

    # evaluate spline at a given x
    def spline_eval(xi):
        idx = np.searchsorted(x, xi) - 1
        idx = np.clip(idx, 0, n - 2)
        xi = xi - x[idx]
        return a[idx] + b[idx] * xi + c[idx] * xi ** 2 + d[idx] * xi ** 3

    return spline_eval


# test
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])


spline = cubic_spline(x, y)

# evaluate at various points
x_vals = np.linspace(x.min(), x.max(), 100)
y_vals = np.array([spline(val) for val in x_vals])

import matplotlib.pyplot as plt

plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_vals, y_vals, label='Cubic Spline')
plt.legend()
plt.show()



#  x and y are time and resource levels respectively
#spline_function = cubic_spline(x, y)

#evaluate the spline at a new point
#new_x_points = np.linspace(np.min(x), np.max(x), num=500)
#estimated_resources = np.array([spline_function(xi) for xi in new_x_points])