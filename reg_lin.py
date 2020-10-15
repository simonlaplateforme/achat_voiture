import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import pandas as pd

car_data = pd.read_csv('carData.csv')

Year = car_data["Year"]
Selling_Price = car_data["Selling_Price"]

# Numpy:

fit = np.polyfit(Year, Selling_Price, 1)
reg_np = [fit[0] * i + fit[1] for i in Year]
plt.figure(1)
plt.title("regression linéaire numpy")
plt.scatter(Year, Selling_Price)
plt.plot(Year, reg_np)
plt.show()


# Scipy:
slope, intercept, r_value, p_value, std_err = stats.linregress(Year, Selling_Price)
reg_sp = [slope * i + intercept for i in Year]
plt.figure(2)
plt.title("regression linéaire Scipy")
plt.scatter(Year, Selling_Price)
plt.plot(Year, reg_sp)
plt.show()


# sklearn:

Year_sk = [[i] for i in Year]
reg_sk = LinearRegression().fit(Year_sk, Selling_Price).predict(Year_sk)
plt.figure(3)
plt.title("regression linéaire sklearn")
plt.scatter(Year, Selling_Price)
plt.plot(Year, reg_sk)
plt.show()
