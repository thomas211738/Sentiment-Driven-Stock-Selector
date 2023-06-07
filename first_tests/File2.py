
import yfinance as yf
import datetime
import csv

def demo_read_csv(filename):
    scores = []
    with open(filename, mode='r') as my_csv:
        reader = csv.reader(my_csv)
        for record in reader:
            scores.append(float(record[0]))
    return scores


def write_to_csv(data):
    with open('test.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Column 1', 'Column 2', 'Column 3'])  # Write header row
        
        for i, row in enumerate(data):
            writer.writerow(['', row, ''])  # Write data row with empty values in column 1 and 3

# Example data

def append_to_csv(data):
    existing_data = []

    # Read the existing data from the CSV file
    with open('output.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        existing_data = list(reader)

    # Append new data to column 2
    for i, row in enumerate(existing_data):
        if i < len(data):
            row.append(data[i])
        else:
            row.append('')

    # Write the updated data back to the CSV file
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(existing_data)

# Example data to append to column 2
new_data = ['New Data 1', 'New Data 2', 'New Data 3']

append_to_csv(new_data)
data = demo_read_csv("profits.csv")

write_to_csv(data)
