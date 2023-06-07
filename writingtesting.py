import csv
import pandas as pd
import numpy as np
from test2 import fdemo_read_csv
import datetime

def demo_write_csv(filename, vals1):
    with open(filename, mode = 'a', newline='') as my_csv:
        
        writer = csv.writer(my_csv)
        writer.writerow([vals1])
        
def add_arrays_to_columns(filename, arrays, header):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader) # Read all rows
    # Combine existing rows with new arrays
   
    rows[0].append(header)
    for i in range(1,len(rows)):
        rows[i].append(arrays[i-1])
        
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)    
        

        

percentage = fdemo_read_csv('CSVs/percentage.csv')
profits = fdemo_read_csv('CSVs/profits.csv')
scores = fdemo_read_csv('CSVs/scores_data.csv')

# demo_write_csv('CSVs/output.csv', f'scores {datetime.date.today()}')

# for i in range(len(percentage)):
#     demo_write_csv('CSVs/output.csv', scores[i])
    
add_arrays_to_columns('CSVs/output.csv', scores, f'scores {datetime.date.today()}')
add_arrays_to_columns('CSVs/output.csv', profits, f'profits {datetime.date.today()}')
add_arrays_to_columns('CSVs/output.csv', percentage, f'percentage {datetime.date.today()}')




    
    

    