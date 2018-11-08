import csv

try:
    csvfile = open('bill.csv', newline='')
except FileNotFoundError:
    print('Failed to open file')
else:
    total = 0
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
        total += float(row[1])
    csvfile.close()
    print("Total:", total)
