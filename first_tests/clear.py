import csv
def clear(filename):
    with open(filename, 'w') as file:
        file.truncate(0)
clear("CSVs/percentage.csv")
clear("CSVs/scores_data.csv")
clear("CSVs/profits.csv")