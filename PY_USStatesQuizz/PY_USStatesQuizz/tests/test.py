import csv
import pandas
PATH_TO_FILE = "./tests/weather_data.csv"
#with open(file = PATH_TO_FILE, mode = "r") as file:
#    for line in file:
#        weather_data.append(line.strip("\n"))

#with open(file = PATH_TO_FILE, mode = "r") as file:
#    weather_data = csv.reader(file)
#    temperatures = []
#    for row in weather_data:
#        print(row)
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))

data = pandas.read_csv(PATH_TO_FILE)
print(data)
print("--------------")
for item in data:
    print(item)
print("--------------")
print(data["temp"])
print("--------------")
for key in data:
    print(data[key])
    print("--------------")

print(data.to_dict())
value = 0
temperature = data["temp"].to_list()

mean = sum(temperature)/len(temperature)
print(mean)
print("average: ", data["temp"].mean())
print("max: ", data["temp"].max())
print(data[data.day == "Monday"])
print(data[data.condition == "Sunny"])

#get day with highest temperature
print(data[data.temp == data["temp"].max()])

#dataframe from a scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [32, 12, 54]
}
data2 = pandas.DataFrame(data_dict)
print(data2)
data2.to_csv("test.csv")