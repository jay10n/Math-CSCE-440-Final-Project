import numpy as np

def romberg_integration(a, b, n):
    def f(x):
        return 3**x 
    
    R = np.zeros((n, n)) 
    h = b - a
    R[0, 0] = 0.5 * h * (f(a) + f(b))
    
    for i in range(1, n):
        h /= 2
        sum_val = 0
        for k in range(1, 2**(i-1) + 1):
            sum_val += f(a + (2*k - 1) * h)
        R[i, 0] = 0.5 * R[i-1, 0] + h * sum_val
        
        for j in range(1, i + 1):
            R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1) 
    return R

a = 0
b = 4
n = 3

romberg_table = romberg_integration(a, b, n)
print("Romberg Integration Table:")
print(romberg_table)
