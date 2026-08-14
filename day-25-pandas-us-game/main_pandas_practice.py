# import csv
# with open("./weather_data.csv") as weather_data:
#     data_lines = csv.reader(weather_data)
#    #data_lines = weather_data.readlines() #when for txt files
#     temperatures = []
#     for row in data_lines:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)

# data_dict = data.to_dict()
# print(f"\n{data_dict}")
#
# temp_list = data["temp"].to_list()
# print(f"\n{temp_list}")

#get avg of temps
# total_temp = sum(temp_list)
# temp_count = len(temp_list)
# avg_temp = total_temp / temp_count
# print(f"Average Temperature in last {temp_count} days = {avg_temp.__round__(2)}")
#instead of writing 4 lines of above to get avg temp, just 1 line w/ lib func:
print(f"Average Temperature in last {len(data["temp"])} days = {data["temp"].mean().__round__(2)}")
#find max temp
print(f"Max Temperature in last {len(data["temp"])} days = {data["temp"].max()}")

# remember that data["temp"] is same as data.temp

#print data in a specific row
print(data[data.day == "Monday"])
#print row with max temp
print(data[data.temp == data.temp.max()])
# convert monday's temp from celcius to F
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * (9/5) + 32
# print(f"\n Converted temp from C = {monday_temp} to F = {monday_temp_F}")
#
# OR make the C to F conversion within table
# data.temp = data.temp.astype(float) # to avoid data type problems w int/float
# data.loc[data.day == "Monday", "temp"] = data.loc[data.day == "Monday", "temp"].iloc[0] * 9/5 + 32
# print(data[data.day == "Monday"])

#if you want to make the whole temp column converted to F
# data.temp = data.temp * 9/5 + 32
# print(data.temp)
#you can also make a new column for F, in addition to C
data["temp_in_F"] = data.temp * 9/5 + 32
print(data)

#you can rename columns
data = data.rename(columns={"temp": "temp_in_C"})
#you can reorder columns
data = data[["day", "condition", "temp_in_C", "temp_in_F"]]
print(data)
