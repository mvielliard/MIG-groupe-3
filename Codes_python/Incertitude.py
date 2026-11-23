x = [15.29E-3,2.39E-6]
u = [5E-5/(3**0.5),1E-6/(0.3**0.5)]
dx = 1E-15

def f(x):
    return x[0]*x[1]

def drond(f,dx,x,i): 
    N = len(x)
    y = [0]*N
    for j in range(N):
        y[i] = x[i]
    y[i] = x[i] + dx
    return (f(y)-f(x))/dx
    

def incertitude(f,x,u,dx):
    N = len(x)
    v = 0
    for i in range(N):
        v = v + (drond(f,dx,x,i)*u[i])**2
    return v**0.5