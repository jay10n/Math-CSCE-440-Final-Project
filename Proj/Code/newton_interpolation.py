
import numpy as np

def newton_interpolation(xs, fs, x):
    n = len(xs)
    F = np.zeros((n, n))
    F[:, 0] = fs 
    
    for i in range(1, n):
        for j in range(1, i+1):
            F[i, j] = (F[i, j-1] - F[i-1, j-1]) / (xs[i] - xs[i-j])
    approx_value = F[0, 0]
    for i in range(1, n):
        term = F[i, i]
        for j in range(i):
            term *= (x - xs[j])
        approx_value += term
    
    return approx_value

# the function we gonna use as a base
def f(x):
    return 2.0**x

# add the array of data we need to work with 
xs = np.array([-3, -2, -1, 0, 1])
fs = [f(x) for x in xs]

approx_value_sqrt2 = newton_interpolation(xs, fs, np.sqrt(2))

print(f'newton approximation {approx_value_sqrt2:.16}')
