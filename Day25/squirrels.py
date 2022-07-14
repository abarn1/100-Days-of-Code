import pandas as pd
squirrel_data = pd.read_csv("./Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

def get_count_squirrels(fur_color, data):
    """
    Return the number of squirrels in the data with the given fur color.
    """
    
    return data[data["Primary Fur Color"] == fur_color].count()["Primary Fur Color"]

get_count_squirrels("Gray", squirrel_data)
squirrel_count = []
color_list = squirrel_data["Primary Fur Color"].dropna().unique().tolist()
for color in color_list:
    squirrel_count.append(get_count_squirrels(color, squirrel_data))
squirrel_count = [color_list, squirrel_count]
squirrel_count = pd.DataFrame(squirrel_count).T
squirrel_count.columns = ["Primary Fur Color", "Count"]
squirrel_count.to_csv("./Day25/squirrel_count.csv")