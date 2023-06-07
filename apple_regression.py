
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
import matplotlib.pyplot as plt
import csv
import seaborn as sns
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


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

tracker = 1
for i in range(len(apple_row)):
    if i == tracker:
        tracker+=3
        X.append(float(apple_row[i-1]))
        Y.append(float(apple_row[i+1]))
        
print(X)
print(Y)   
    
    
    



# for i in range(len(apple_row)):
#     if (i % 2 == 0):
#         X.append(float(apple_row[i]))
#     else:
#         Y.append(float(apple_row[i]))
        



X = np.array(X).reshape(-1,1)
Y = np.array(Y)


# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, Y)
regr_2.fit(X, Y)

# Predict
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)

# Plot the results
plt.figure()
plt.scatter(X, Y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()



   

    
            
