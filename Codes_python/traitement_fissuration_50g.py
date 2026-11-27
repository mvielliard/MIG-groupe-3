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
    x_moy = np.mean(x)
    u_x = np.sum((x - x_moy)**2)/(N-1)
    return (u_x/N)**0.5

mesure_1 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_1.xlsx')
mesure_1 = mesure_1.T
mesure_2 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_2.xlsx')
mesure_2 = mesure_2.T
mesure_3 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_3.xlsx')
mesure_3 = mesure_3.T 
mesure_4 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_4.xlsx')
mesure_4 = mesure_4.T 
mesure_5 = pd.read_excel('Data\\Mesures_indenteur\\Filiation_5.xlsx')
mesure_5 = mesure_5.T 



mesure = pd.concat([mesure_1, mesure_2,mesure_3,mesure_4,mesure_5], ignore_index = True)
mesure.columns = ['Distance','Dia 1', 'Diag 2', 'Diag moy', 'Durete', 'Fissuration','Exploitable']
mesure['Fissuration'] = mesure['Fissuration'].astype(int)
mesure['Exploitable'] = mesure['Exploitable'].astype(int)

N = len(mesure)

p = mesure['Fissuration'].mean()

mesure_exploitable = mesure[mesure['Exploitable'] == 1]
n = N - mesure_exploitable['Fissuration'].sum()
mesures_durete = np.zeros(n)
k = 0
for i in range(N):
    if mesure.loc[i,'Fissuration'] == 0:
        mesures_durete[k] = mesure_exploitable.loc[i, 'Durete']
        k = k + 1

plt.plot(mesures_durete)
plt.show()
durete = mesures_durete.mean()
incertitude = incertitude_type(mesures_durete)


mesures_latex = mesure[['Durete','Fissuration']]
mesures_latex.columns= ['Durete (HV)','Fissuration']
mesures_latex['Fissuration'] = mesures_latex['Fissuration'].astype(str)
for i in range(N):
    if mesures_latex.loc[i,'Fissuration'] == '0':
        mesures_latex.loc[i,'Fissuration'] = 'Non'
    else:
        mesures_latex.loc[i,'Fissuration'] = 'Oui'


df = pd.DataFrame([[durete, incertitude, p]], columns = ['Durete moyenne', 'Incertitude','Probabilité de fissure'])
# print(df)

print(mesures_durete)


