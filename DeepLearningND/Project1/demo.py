import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()


#read data
dataframe = pd.read_csv('challenge_dataset.txt')
x_values = dataframe[[0]]
y_values = dataframe[[1]]

#train model on data
model = linear_model.LinearRegression()
model.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, model.predict(x_values))
plt.show()

print(model.predict([ [127], [248] ]))
