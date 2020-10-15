import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class LinearRegression:
    def __init__(self, n_iter):
        self.n_iter = n_iter
        self.alpha = 0
        self.beta = 0

    def fit(self, x, y):
        alpha = 0
        temp = 0
        moy_x = sum(x) / len(x)
        moy_y = sum(y) / len(y)

        for iteration in range(self.n_iter):
            alpha += (x[iteration] - moy_x) * (y[iteration] - moy_y)
            temp += (x[iteration] - moy_x) ** 2
        alpha /= temp
        beta = moy_y - alpha * moy_x
        self.alpha = alpha
        self.beta = beta

    def plot(self, x=None, y=None):
        plt.figure()
        plt.title("regression linéaire de coefficient alpha= {} et beta= {}" . format(self.alpha, self.beta))
        if x.size == 0:
            x_droite = [i for i in range(11)]
        else:
            plt.scatter(x, y)
            x_droite = [i for i in range(x.min(), x.max())]
        y_droite = [self.alpha * i + self.beta for i in x_droite]
        plt.plot(x_droite, y_droite)
        plt.show()


car_data = pd.read_csv("carData.csv")
reg_lin = LinearRegression(100)
reg_lin.fit(car_data["Year"], car_data["Selling_Price"])
reg_lin.plot(np.array(car_data["Year"]), np.array(car_data["Selling_Price"]))
