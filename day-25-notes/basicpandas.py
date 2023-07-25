import pandas

data = pandas.read_csv('weather_data.csv')
# data = pandas dataframe object (2d array)
print (type(data))

print(type(data['temp']))
#this will be a panda series data type (1d array)

data_dict = data.to_dict() # convert dataframes to dictionaries
print(data_dict)

temp_list = data['temp'].to_list() # convert series to lists
print(len(temp_list))

average = sum(temp_list) / len(temp_list)
print (average)

print(data['temp'].max())

print(data['temp']) # instead of this
print(data.temp) # you can also do this (this is case sensitive btw)

print(data[data.temp == data.temp.max()])

print((data[data.day == 'Monday'].temp * (9/5)) + 32)

# create a dataframe from scratch

dictionary = {
    "fellas":['john', 'alex', 'mark'],
    'weight':[147, 178, 162],
}
custom_dataframe = pandas.DataFrame(dictionary)
print(custom_dataframe)
custom_dataframe.to_csv('somenew_data.csv')