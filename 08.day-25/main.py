# Part 1:
# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# Part 2:
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# Part 3:

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)
#
# temp_avg_pandas = data["temp"].mean()
# print(temp_avg_pandas)
#
# temp_max_pandas = data["temp"].max()
# print(temp_max_pandas)
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in row
# print(data[data.day == "Monday"])
#
# # Get data in row with max temp
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(f"Monday temp in F: {monday_temp_F}")
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv", index=False)

# Part 4:
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv", index=False)
