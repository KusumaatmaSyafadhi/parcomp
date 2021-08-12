import csv

contacts = []

with open('Data1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        contacts.append(row)

print(contacts)