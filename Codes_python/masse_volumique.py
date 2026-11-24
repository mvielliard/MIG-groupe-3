import pandas as pd 
import matplotlib.pyplot as plt

sous_eau = pd.read_csv("Codes_python\\verre-sous-eau.csv", delimiter = ';', decimal = ',',index_col = 'Temps')
sans_eau = pd.read_csv("Codes_python\\verre-sans-eau.csv", delimiter = ';', decimal = ',', index_col = 'Temps')
sans_eau = sans_eau*-1
sans_eau = sans_eau.loc[9:30,:]
sous_eau = sous_eau*-1
plt.plot(sous_eau['Force_50N_[N]'])
plt.plot(sans_eau['Force_50N_[N]'])
plt.show()
print(sous_eau.describe())
print(sans_eau.describe())