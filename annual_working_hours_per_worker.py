import csv

data = []
with open('annual-working-hours-per-worker.csv',mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        data.append(lines)
country,hours = [],[]
for i in data[1:]:
    country.append(i[0])
    hours.append(float(i[3]))
dict_annual_working_hours_per_worker = {}
for i in range(len(country)):
    if country[i] not in dict_annual_working_hours_per_worker:
        dict_annual_working_hours_per_worker[country[i]] = hours[i]
    else:
        dict_annual_working_hours_per_worker[country[i]]+=hours[i]
howmanytimesdoesitappear = {}
for i in country:
    if i in howmanytimesdoesitappear:
        howmanytimesdoesitappear[i]+=1
    else:
        howmanytimesdoesitappear[i]=1
for i in dict_annual_working_hours_per_worker:
    dict_annual_working_hours_per_worker[i]/=howmanytimesdoesitappear[i]
    dict_annual_working_hours_per_worker[i] = int(dict_annual_working_hours_per_worker[i])

def get():
    global dict_annual_working_hours_per_worker
    return dict_annual_working_hours_per_worker