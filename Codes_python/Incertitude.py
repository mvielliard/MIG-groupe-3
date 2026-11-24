rs = [20.60,0.006163973668461999]  #épaisseur , temps
delta_rs = [0.2, 1E-4]
rl = [20.60,0.0035615491009681885]
delta_rl = [0.2, 1E-4]
dx = 1E-10


roh_eau = 1000 #kg/m^3
F = [0.9608, 0.6523] #F_air, F_eau
delta_F = [5E-4, 5E-4]




def v(r):
    return r[0]/r[1]

def roh(F):
    return roh_eau/(1-(F[1]/F[0]))
def E(x):
    return (x[0]*x[2]**2*(3*x[1]**2-4*x[2]**2))/(x[1]**2 - x[2]**2)
def nu(x):
    return (x[0]**2-2*x[1]**2)/(2*(x[0]**2 - x[1]**2))


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

x1 = [3107.0, 5784, 3301] # roh, cl, cs
delta_x1 = [incertitude(roh,F,delta_F,dx), incertitude(v,rl,delta_rl,dx), incertitude(v,rs,delta_rs,dx)]

x2 = [5784, 3301] # roh, cl, cs
delta_x2 = [incertitude(v,rl,delta_rl,dx), incertitude(v,rs,delta_rs,dx)]