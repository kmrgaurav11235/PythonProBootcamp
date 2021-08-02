import pandas

census_data_frame = pandas.read_csv(filepath_or_buffer="2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
unique_fur_colors = census_data_frame["Primary Fur Color"].unique()
fur_color_count_dict = {
    "Fur Color": [],
    "Count": [],
}

for fur_color in unique_fur_colors:
    if fur_color != fur_color:
        # To get rid on NaN
        pass
    else:
        count = len(census_data_frame[census_data_frame["Primary Fur Color"] == fur_color])
        print(f"{fur_color} \t {count}")
        fur_color_count_dict["Fur Color"].append(fur_color)
        fur_color_count_dict["Count"].append(count)

fur_color_count_data_frame = pandas.DataFrame(fur_color_count_dict)
fur_color_count_data_frame.to_csv("03_squirrel_unique_fur_colors.csv")