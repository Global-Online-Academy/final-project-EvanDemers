import csv

data = []
with open('gdp_1960_2020.csv',mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        data.append(lines)

country,gdp = [],[]
for i in data[1:]:
    country.append(i[2])
    gdp.append(int(i[4]))

dictionary = {}
for i in range(len(country)):
    if country[i] not in dictionary:
        dictionary[country[i]]=gdp[i]
    else:
        dictionary[country[i]] += gdp[i]

num = {}
for i in range(len(country)):
    if country[i] not in num:
        num[country[i]] = 1
    else:
        num[country[i]] += 1

for i in dictionary:
    dictionary[i] = dictionary[i] / num[i]
    dictionary[i] = int(dictionary[i])

def get():
    global dictionary
    return dictionary