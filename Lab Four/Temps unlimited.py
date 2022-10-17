from statistics import mean
def average(temps):
    mintemps = min(temps)
    maxtemps = max(temps)
    meantemps1 = mean(temps)
    choice = input("Would you like the min, max or mean?")
    if choice.title() == "Min":
        print(mintemps)
    if choice.title() == "Max":
        print(maxtemps)
    if choice.title() == "Mean":
        print(meantemps)

temps = []

while True:
    temp = input("Enter the tempreture in Celsius Degrees")
    if temp == "":
        break
    else:
        temps.append(int(temp))

average(temps)
