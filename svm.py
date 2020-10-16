from sklearn import svm
import pandas as pd
import matplotlib.pyplot as plt

car_data = pd.read_csv("carData.csv")
Year = car_data.Year
Year_svm = [[year] for year in Year]
Price = car_data.Selling_Price

reg_svm = svm.SVR(kernel="linear")
reg_svm.fit(Year_svm, Price)
price_svm = reg_svm.predict(Year_svm)
print(reg_svm.score(Year_svm, Price))

plt.figure(5)
plt.scatter(Year, Price)
plt.plot(Year, price_svm, "r")
plt.show()
