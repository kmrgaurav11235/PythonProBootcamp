# Work with CSV using open() function
# with open(file="weather_data.csv", mode="r") as csv_file:
#     csv_data_list_with_whitespace = csv_file.readlines()
#
# csv_data_list = []
# for row in csv_data_list_with_whitespace:
#     csv_data_list.append(row.strip())
#
# print(csv_data_list)

import csv

with open(file="weather_data.csv", mode="r") as csv_file:
    data = csv.reader(csv_file)
    temperatures = []

    is_header = True
    for row in data:
        print(row)
        if is_header:
            is_header = False
        else:
            temperatures.append(int(row[1]))

    print(temperatures)
