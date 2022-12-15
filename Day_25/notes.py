# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         # print(row)
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# # A DataFrame
# data_dict = data.to_dict()
# print(data_dict)
#
# # A Series
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # Average Temperatures
# avg_temp = sum(temp_list)/len(temp_list)
# print(round(avg_temp))
#
# # Average Temperature by using Series method
# print(data["temp"].mean())
#
# # Find largest value in Series
# print(data["temp"].max())
#
# #Get Data in Columns (Each column is a Series)
# print(data["condition"])
# # AN EASIER WAY: Pandas automatically makes column labels attributes
# print(data.condition)

# Get Data From Column
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# #Convert from Celsius to Farenheit
# print(monday.temp * 1.8 + 32)

#CREATE A DATAFRAME FROM SCRATCH
# data_dict = {
#     "students": ["Amy", "Jason", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# #Convert in CSV File
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_data_count = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(squirrel_data_count)
df.to_csv("squirrel_count.csv")



