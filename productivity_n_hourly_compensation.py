import csv

data = []
with open('productivity_n_hourly_compensation.csv',mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        data.append(lines)

prod,comp = [],[]
for i in data[1:]:
    prod.append(float(i[1]))
    comp.append(float(i[3]))

def get():
    global prod,comp
    return prod,comp