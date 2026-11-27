import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def drond(f,dx,x,i): #Dériivation par rapport à la ième variable
    N = len(x)
    y = [0]*N
    for j in range(N):
        y[j] = x[j]
    y[i] = x[i] + dx
    a = f(y) - f(x)
    return a/dx

 

def propagation_des_erreurs(f,x,u,dx): #Calcul de l'incertitude sur f(x) en fonction de celle sur x
    N = len(x)
    v = 0
    for i in range(N):
        v = v + (drond(f,dx,x,i)*u[i])**2
    return v**0.5

def incertitude_type(x): #Calcul l'incertitude associé a une sére de N mesures
    N = len(x)
    x_moy = np.mean(x)
    u_x = np.sum((x - x_moy)**2)/(N-1)
    return (u_x/N)**0.5


mesure_1 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_1_200g.xlsx')
mesure_1 = mesure_1.T
mesure_2 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_2_200g.xlsx')
mesure_2 = mesure_2.T
mesure_3 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_3_200g.xlsx')
mesure_3 = mesure_3.T 
mesure_4 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_4_200g.xlsx')
mesure_4 = mesure_4.T 

# print(mesure_4)
# print(mesure_3)

mesure = pd.concat([mesure_1, mesure_2,mesure_3,mesure_4], ignore_index = True)
mesure.columns = ['Distance','c1', 'c2', 'cmoy', 'Durete','amoy', 'Fissuration','Exploitable']
# print(mesure)
mesure['Fissuration'] = mesure['Fissuration'].astype(int)
mesure['Exploitable'] = mesure['Exploitable'].astype(int)
mesure_exploitable = mesure[mesure['Exploitable'] == 1]


p_fissure = mesure['Fissuration'].mean()
p_exploitable = mesure['Exploitable'].mean()

durete = 749.676036  #En HV
E = 8.692147e+10 #Module de Young en GPa
g = 9.81 #ms^-2
F = 200*g #Force appliqué en N
xi = 0.016 #



N1 = len(mesure)
N2 = len(mesure_exploitable)
n = mesure_exploitable['Fissuration'].sum()
mesure_exploitable = mesure_exploitable.reset_index()
mesure_c = np.zeros(n)
mesure_a = np.zeros(n)
k = 0
for i in range(N2):
    if mesure_exploitable.loc[i,'Fissuration'] == 1:
        mesure_c[k] = mesure_exploitable.loc[i,'cmoy']
        mesure_a[k] = mesure_exploitable.loc[i,'amoy']
        k = k + 1
       
mesure_tenacite = xi*((E/durete)**0.5)*F/(mesure_c**0.5)
mesure_ratio = mesure_c/mesure_a
mesure_ratio = mesure_ratio[~np.isnan(mesure_ratio)]

tenacite = mesure_tenacite.mean()
incertitude_tenacite = incertitude_type(mesure_tenacite)
ratio = mesure_ratio.mean()
incertitude_ratio = incertitude_type(mesure_ratio)

df = pd.DataFrame([[tenacite,incertitude_tenacite,ratio,incertitude_ratio,p_fissure,p_exploitable]], 
                  columns = ['Tenacité','Incertitude Tenacité','c/a','incertitude c/a','Pfissure','exploitable'])

print(df)
