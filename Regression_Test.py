
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import csv
import seaborn as sns
import numpy as np


def fdemo_read_csv(filename):
    lists = []
    with open(filename, mode='r') as my_csv:
        reader = csv.reader(my_csv)
        for record in reader:
            lists.append(float(record[0]))
    return lists


rng = np.random.RandomState(1)

X_scores = np.array(fdemo_read_csv("scores_data.csv")).reshape(-1,1)
Y_profits = np.array(fdemo_read_csv("profits.csv"))


regr_1 = DecisionTreeRegressor(max_depth=4)
regr_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=300, random_state=rng)

regr_1.fit(X_scores, Y_profits)
regr_2.fit(X_scores, Y_profits)

y_1 = regr_1.predict(X_scores)
y_2 = regr_2.predict(X_scores)

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X_scores, Y_profits, color=colors[0], label="training samples")
#plt.plot(X_scores, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X_scores, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("Scores")
plt.ylabel("Profits")
plt.title("Score VS Profits Regression")
plt.legend()
plt.show()

