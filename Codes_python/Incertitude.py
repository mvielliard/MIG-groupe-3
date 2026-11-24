# x = [20.60,0.00364666312621703]
# u = [0.2, 1E-4]
# dx = 1E-10
r = [20.60,0.006163973668461999]
delta_r = [0.2, 1E-4]
dx = 1E-10


roh_eau = 1000 #kg/m^3



def v(r):
    return x[0]/x[1]

def roh(F):
    return roh_eau/(1-(F[1]/F[0]))

def drond(f,dx,x,i): 
    N = len(x)
    y = [0]*N
    for j in range(N):
        y[j] = x[j]
    y[i] = x[i] + dx
    print (y)
    print (x)
    a = f(y) - f(x)
    return a/dx


def incertitude(f,x,u,dx):
    N = len(x)
    v = 0
    for i in range(N):
        v = v + (drond(f,dx,x,i)*u[i])**2
    return v**0.5