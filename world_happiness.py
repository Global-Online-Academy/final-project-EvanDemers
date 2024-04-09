import csv

data = []
with open('2019.csv',mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        data.append(lines)
country,score=[],[]
for i in data[1:]:
    country.append(i[1])
    score.append(float(i[2]))

di = {}
for i in range(len(country)):
    di[country[i]] = score[i]

def get():
    global di
    return di