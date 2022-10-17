from statistics import mean
temp = []
while len(temp) != 6:
    temp.append(int(input("Enter the tempreture in Celsius Degrees")))

mintemp = min(temp)
maxtemp = max(temp)
meantemp = mean(temp)
choice = input("Would you like the min, max or mean?")
if choice.title() == "Min":
    print(mintemp)
if choice.title() == "Max":
    print(maxtemp)
if choice.title() == "Mean":
    print(meantemp)

