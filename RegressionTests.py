
from sklearn import svm
import matplotlib.pyplot as plt
import csv
import seaborn as sns
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import pandas as pd 


def read_csv_row(filename, row_number):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)  # Convert the reader object to a list of rows
        if 0 <= row_number < len(rows):
            return rows[row_number]
        else:
            return None

def compRegression(ticker: str):
    df = pd.read_csv("CSVs/project_data.csv")
    index = ticker
    df_list = df['Ticker'].values.tolist()
    indices = df_list.index(index)+1
    company_row = read_csv_row('CSVs/project_data.csv',indices)
    company_row = company_row[3:]

    X = []
    Y = []

    tracker = 1
    for i in range(len(company_row)):
        if i == tracker:
            tracker+=3
            X.append(float(company_row[i-1]))
            Y.append(float(company_row[i+1]))   

    X = np.array(X)
    Y = np.array(Y)
    # Calculate the coefficients of the line of best fit (linear regression)
    coefficients = np.polyfit(X, Y, 1)
    m = coefficients[0]  # slope
    b = coefficients[1]  # y-intercept
    x_extended = np.linspace(min(X)-0.3 , max(X)+0.3 , 100)
    # Calculate the corresponding y-values using the line's equation
    y_extended = m * x_extended + b
    #Plot the results
    plt.figure()
    plt.scatter(X, Y, s=20, edgecolor="black", c="darkorange", label="data")
    plt.plot(x_extended, y_extended, color='red', label='Line of Best Fit')
    #plt.xlim(-1,1)
    plt.xlabel("scores")
    plt.ylabel("percent change")
    plt.title("Scores vs prices for " + str(ticker))
    plt.legend()
    plt.show()

def SlopeR2():
    coef = []
    for j in range(1,504):
        rowOG = read_csv_row('CSVs/project_data.csv',j)
        row = rowOG[3:]
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
        m = coefficients[0]  #gets the slope for the compnay

        regression_model = LinearRegression()
        regression_model.fit(X.reshape(-1, 1), Y)
        r2 = r2_score(Y, regression_model.predict(X.reshape(-1, 1))) #gets the r2 score for the company

        dict = {
            "Company Name": rowOG[1],
            "Company Row": j-1,
            "Slope": m,
            "R2": r2
        }
        coef.append(dict)
    return coef

companyValues = SlopeR2()
filtered_list = [d for d in companyValues if d['Slope'] >= 0]
filtered_list = [d for d in filtered_list if d['R2'] >= 0.1]
sorted_list = sorted(filtered_list, key=lambda x: x['R2'], reverse = True)

print(sorted_list)
print(len(sorted_list))
def graph():
    df = pd.read_csv("CSVs/project_data.csv")
    df = df["Ticker"]
    ticker = df.iloc[297] # enter the index of the company you want to get
    compRegression(ticker) # or enter the company ticker
graph()

    


