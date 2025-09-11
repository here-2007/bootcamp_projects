import csv
def avg(row):
    daily=0
    monthly=0
    weekly=0
    
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        ...
