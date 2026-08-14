import pandas as pd

data_set = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_set = data_set.dropna(subset="Primary Fur Color")

gr_sq_count = len(data_set[data_set["Primary Fur Color"] == "Gray"])
cinnamon_sq_count = len(data_set[data_set["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(data_set[data_set["Primary Fur Color"] == "Black"])

data_dict = {"Fur Colour": ["Gray", "Cinnamon", "Black"],
             "Count": [gr_sq_count, cinnamon_sq_count, black_sq_count],
}

squirrel_count_compact_set = pd.DataFrame(data_dict)
squirrel_count_compact_set.to_csv("squirrel_count.csv")

