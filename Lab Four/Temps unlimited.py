from statistics import mean
def average(temps):
    mintemps = min(temps)
    maxtemps = max(temps)
    meantemps = mean(temps)
    choice = input("Would you like the min, max or mean or none?")
    if choice.title() == "Min":
        print(mintemps)
        average(temps)
    if choice.title() == "Max":
        print(maxtemps)
        average(temps)
    if choice.title() == "Mean":
        print(meantemps)
        average(temps)
    if choice.title() == "None":
        quit()

temps = []

while True:
    temp = input("Enter the tempreture in Celsius Degrees")
    if temp == "":
        break
    else:
        temps.append(int(temp))

average(temps)
