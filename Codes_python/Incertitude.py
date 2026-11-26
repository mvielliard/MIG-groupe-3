import pandas as pd

def drond(f,dx,x,i): ##Dériivation par rapport à la ième variable
    N = len(x)
    y = [0]*N
    for j in range(N):
        y[j] = x[j]
    y[i] = x[i] + dx
    a = f(y) - f(x)
    return a/dx


def incertitude(f,x,u,dx): #Calcul de l'incertitude sur f(x) en fonction de celle sur x
    N = len(x)
    v = 0
    for i in range(N):
        v = v + (drond(f,dx,x,i)*u[i])**2
    return v**0.5


## Fonctions utilisés pour trouver les valeurs ##
def t(e,c):
    return(e/c)
def v(r):
    return r[0]/r[1]
def roh(F):
    return roh_eau/(1-(F[1]/F[0]))
def E(x):
    return (x[0]*x[2]**2*(3*x[1]**2-4*x[2]**2))/(x[1]**2 - x[2]**2)
def nu(x):
    return (x[0]**2-2*x[1]**2)/(2*(x[0]**2 - x[1]**2))

## Valeurs experimentales à modifier ##

e = 20.60 #epaisseur mesurée en mm
delta_e = 0.2 #incertitude sur la mesure en mm
cl = 5.784000e+03 #célerité des ondes longitudinales en m/s
cs = 3.342000e+03 #célerité des ondes de cisaillement en m/s
f = 5E3 #fréquece en khz
F = [0.9608, 0.6523] #F_air, F_eau
delta_F = [1E-2, 1E-2] #F_air, F_eau


rs = [e,t(e,cs)]  #épaisseur , temps
delta_rs = [delta_e, 1/(2*f)] 
rl = [e,t(e,cl)]
delta_rl = [delta_e, 1/(2*f)]
dx = 1E-10

roh_eau = 1000 #kg/m^3

x1 = [roh(F), cl, cs] # roh, cl, cs
delta_x1 = [incertitude(roh,F,delta_F,dx), incertitude(v,rl,delta_rl,dx), incertitude(v,rs,delta_rs,dx)]

x2 = [cl, cs] # cl, cs
delta_x2 = [incertitude(v,rl,delta_rl,dx), incertitude(v,rs,delta_rs,dx)]

df = pd.DataFrame([['cl',v(rl),incertitude(v, rl, delta_rl, dx)],
                   ['cs',v(rs),incertitude(v, rs, delta_rs, dx)],
                   ['roh',roh(F),incertitude(roh,F,delta_F,dx)],
                   ['E',E(x1),incertitude(E, x1, delta_x1, dx)],
                   ['nu',nu(x2),incertitude(nu, x2, delta_x2, dx)]],
                  columns = ['Grandeur','Valeur','Incertitude'])
print(df)