import csv

with open("themes/CHI.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count >= 1:
            print(row[0])
        line_count += 1

