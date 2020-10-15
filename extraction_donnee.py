import pandas as pd
import matplotlib.pyplot as plt

car_data = pd.read_csv('carData.csv')

print("Ensemble des colones de la db :\n")
for i in range(len(car_data.columns)):
    print(car_data.columns[i])

print("taille de la base de donnée : {}" . format(car_data.shape))

# Quelle est la moyenne des selling_prices ?
print("Le prix moyen des véhicules est de {}" . format(car_data.loc[:, 'Selling_Price'].mean()))
plt.figure()
plt.title("histogramme des Selling Price")
plt.hist(car_data.loc[:, 'Selling_Price'])
plt.show()

# De meme pour les Present Price:
print("Le prix moyen des véhicules a l'heure actuelle est de {}" . format(car_data.loc[:, 'Present_Price'].mean()))
plt.figure(2)
plt.title("histogramme des prix actuels")
plt.hist(car_data.loc[:, 'Present_Price'])
plt.show()

# On s'interesse aussi au kilometrage des véhicules:
print("Le kilometrage moyen des véhicules est de : {}" . format(car_data.loc[:, 'Kms_Driven']))
plt.figure(3)
plt.title("kilometrage moyen")
plt.hist(car_data.loc[:, 'Kms_Driven'])
plt.show()

