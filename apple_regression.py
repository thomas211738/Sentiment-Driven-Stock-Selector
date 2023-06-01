
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import csv
import seaborn as sns
import numpy as np


def read_csv_row(filename, row_number):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)  # Convert the reader object to a list of rows
        if 0 <= row_number < len(rows):
            return rows[row_number]
        else:
            return None

apple_row = read_csv_row('project_data - Sheet1.csv',1)

apple_row = apple_row[3:]

X = []
Y = []

for i in range(len(apple_row)):
    if (i % 2 == 0):
        X.append(float(apple_row[i]))
    else:
        Y.append(float(apple_row[i]))
        

X = np.array(X).reshape(-1,1)
Y = np.array(Y)

rng = np.random.RandomState(1)

regr_1 = DecisionTreeRegressor(max_depth=4)
regr_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=50, random_state=rng)

regr_1.fit(X, Y)
regr_2.fit(X, Y)

y_1 = regr_1.predict(X)
y_2 = regr_2.predict(X)

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, Y, color=colors[0], label="training samples")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("Scores")
plt.ylabel("Profits")
plt.title("Score VS Profits Regression")
plt.legend()
plt.show()



   

    
            
