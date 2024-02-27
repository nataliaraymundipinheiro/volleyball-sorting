import csv

def readFile(file):
    file = open(file, "r")
    csvreader = csv.reader(file)

    next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    file.close()
    return rows