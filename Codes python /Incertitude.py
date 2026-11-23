import numpy as np

x = (15.29E-3,2.39E-6)
u = (5E-5/(3**0.5),0)
N = 2

def f(x):
    return(x[0]*x[1])

def drond(f,dx,x,i): 
    xi = x[i]
    y = x.copy
    y[i] = x[i] + dx
    return (f(y)-f(x))/dx

def incertitude(f,N,x,u,dx):
    assert len(x) == N :
    v = 0
    for i in range(N):
        v = v + (drond(f,dx,x,i)*u[i])**2
    return v**0.5
