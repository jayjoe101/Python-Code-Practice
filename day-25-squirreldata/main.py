import pandas

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

furcount = {
    'Fur color' : ['Gray', 'Red', 'Black'],
    'Count' : squirrel_data['Primary Fur Color'].value_counts().to_list(),
}

fur_dataframe = pandas.DataFrame(furcount)
fur_dataframe.to_csv('new_furdata.csv')