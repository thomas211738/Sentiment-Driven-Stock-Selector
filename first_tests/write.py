import csv
def demo_write_csv(filename, vals1):
    with open(filename, mode = 'w', newline='') as my_csv:
        writer = csv.writer(my_csv)
        writer.writerow(vals1)
def demo_append_csv(filename, vals1):
    with open(filename, mode = 'a', newline='') as my_csv:
        append = csv.writer(my_csv)
        append.writerow(vals1)

vals1demo = ['a','b','c']
vals2demo = ["c",1,2]
demo_write_csv('fruits.csv',vals1demo)
demo_write_csv('fruits.csv',vals2demo)