import csv
import pandas

PATH_TO_SQUIRREL = "./tests/2018CentralParkSquirelData.csv"

squirrel_data = pandas.read_csv(PATH_TO_SQUIRREL)

#extract the colors of the squirrels
colors = list(set(squirrel_data["Primary Fur Color"]))
colors.pop(0)

squirrel_dict = {
    "fur color:": [],
    "count": []
    }

squirrel_keys = list(squirrel_dict.keys())

#create dictionary of squirrels
for color in colors:
    amount = sum(squirrel_data["Primary Fur Color"] == color)
    squirrel_dict[squirrel_keys[0]].append(color)
    squirrel_dict[squirrel_keys[1]].append(amount)


#gray_ones = sum(squirrel_data["Primary Fur Color"] == "Gray")
#print(gray_ones)
#print(number_of_squirrels)
#print(squirrel_dict)

squirrel_panda = pandas.DataFrame(squirrel_dict)
print(squirrel_panda)
squirrel_panda.to_csv("./tests/SquirrelCount.csv")