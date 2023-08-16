import pandas

squirrel_data_path = "../Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrel_data = pandas.read_csv(squirrel_data_path)

# We can loop over the dataframe

for (index, row) in squirrel_data.iterrows():
    print(row)