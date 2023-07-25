

with open('weather_data.csv', 'r') as file:
    data = file.readlines()
    print (data)

import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    print (data)
    temp = []
    for r in data:
        if r[1].isnumeric():
            temp.append(int(r[1]))
    print (temp)

import pandas

data = pandas.read_csv('weather_data.csv')
print (data['temp'])