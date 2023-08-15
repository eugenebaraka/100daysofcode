import csv

# temperatures = []
# with open("weather_data.csv", "r") as weather_data:
#     data = csv.reader(weather_data)
#     for day in data:
#         if day[1] != 'temp':
#             temperatures.append(int(day[1]))
# print(temperatures)

# import pandas as pd
# data = pd.read_csv("weather_data.csv")
# print(data)

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# data.groupby("Primary Fur Color").agg(func=sum)

