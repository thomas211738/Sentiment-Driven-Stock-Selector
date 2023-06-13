

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

apple_row = read_csv_row('CSVs/project_data.csv',503)

apple_row = apple_row[3:]

X = []
Y = []

tracker = 1
for i in range(len(apple_row)):
    if i == tracker:
        tracker+=3
        X.append(float(apple_row[i-1]))
        Y.append(float(apple_row[i+1]))
        
# print(X)
# print(Y)   

X = np.array(X)
Y = np.array(Y)

# Calculate the coefficients of the line of best fit (linear regression)
coefficients = np.polyfit(X, Y, 1)
m = coefficients[0]  # slope
b = coefficients[1]  # y-intercept

x_extended = np.linspace(min(X)-0.3 , max(X)+0.3 , 100)

# Calculate the corresponding y-values using the line's equation
y_extended = m * x_extended + b

# Plot the results
plt.figure()
plt.scatter(X, Y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(x_extended, y_extended, color='red', label='Line of Best Fit')
plt.xlim(-1,1)
plt.xlabel("scores")
plt.ylabel("percent change")
plt.title("Scores vs prices")
plt.legend()
plt.show()



def coef():
    coef = []
    for j in range(1,504):
        row = read_csv_row('CSVs/project_data.csv',j)
        row = row[3:]

        X = []
        Y = []

        tracker = 1
        for i in range(len(row)):
            if i == tracker:
                tracker+=3
                X.append(float(row[i-1]))
                Y.append(float(row[i+1]))
                
           

        X = np.array(X)
        Y = np.array(Y)
        
       
        coefficients = np.polyfit(X, Y, 1)
        m = coefficients[0]
        coef.append(m)
    return coef
print(coef())
   

    
            
