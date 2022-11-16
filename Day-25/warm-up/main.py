import csv
import pandas

# csv python code
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# pandas python code
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# print as a dictionary
# dictionary = data.to_dict()
# print(dictionary)

# print temperature as a list
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# find the average temp
# total = 0
# for temp in temp_list:
#     total += temp
# length = len(temp_list)
# average = round(total / length)
# print(average)

# find the average temp
# average = round(sum(temp_list) / len(temp_list), 2)
# print(average)

# print the mean and max using pandas
# getting data in a column
# print(data["temp"].mean())
# print(data.temp.max())

# getting data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = int(monday.temp)
# to_fahrenheit = monday_temp * (9 / 5) + 32
# print(to_fahrenheit)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
