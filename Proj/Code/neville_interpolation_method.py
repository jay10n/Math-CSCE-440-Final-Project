import math

def neville(datax, datay, x):
    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i]+ \
                        (datax[i]-x)*p[i+1])/ \
                        (datax[i]-datax[i+k])
    return p[0]

def g(x):
    return 2**x


datax = [-3, -2, -1, 0, 1]

datay = [g(x) for x in datax]


x = 2**0.5

approx_value = neville(datax, datay, x)
print(f'neville methode approxmation: {approx_value}')


principal = 20000
amount = 1200000
periods = 35

def f(i, principal, periods, amount):
    return principal * ((1 + i)**periods - 1) / i - amount

def df(i, principal, periods):
    return principal * (((1 + i)**periods - 1) / i**2 + periods * (1 + i)**(periods-1))

def newton_raphson(f, df, p0, eps, Nmax, principal, periods, amount=None):
    i = 1
    while i <= Nmax:
        p = p0 - f(p0, principal, periods, amount) / df(p0, principal, periods)
        if abs(p - p0) < eps:
            return p
        p0 = p
        i += 1
    return "Failed to find root after Nmax iterations."

root_newton = newton_raphson(f, df, 0.05, 1e-12, 10000, principal, periods, amount)
print(f"Newton's Method least interset {root_newton:.12f}")