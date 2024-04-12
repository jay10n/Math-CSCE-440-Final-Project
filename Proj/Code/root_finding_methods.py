import math

def bisection_method(f, a, b, eps, Nmax):
    
    i = 1
    FA = f(a)
    
    while i <= Nmax:
        p = a + (b - a) / 2
        FP = f(p)
        
        if FP == 0 or (b - a) / 2 < eps:
            return p
        
        i += 1
        
        if FP * FA > 0:
            a = p
            FA = FP
        else:
            b = p
    
    return "Method failed after Nmax iterations."

def newton_raphson(f, df, p0, eps, Nmax):
    
    i = 1
    
    while i <= Nmax:
        p = p0 - f(p0) / df(p0) 
        
        if abs(p - p0) < eps:
            return p
        
        p0 = p 
        i += 1
    
    return "Failed to find root after Nmax iterations."

def secant_method(f, p0, p1, eps, Nmax):
    
    i = 2
    y0 = f(p0)
    y1 = f(p1)
    
    while i <= Nmax:
        if y1 - y0 == 0:
            return "Division by zero encountered. Method failed."
        
        p = p1 - y1 * (p1 - p0) / (y1 - y0) 
        
        if abs(p - p1) < eps:
            return p
        p0, y0 = p1, y1
        p1, y1 = p, f(p)
        
        i += 1
    
    return "Failed to find root after Nmax iterations."
