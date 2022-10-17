def ctof(cel):
    fah = (cel * 1.8) + 32
    print(fah)

def ftoc(fah):
    cel = (fah - 32) / 1.8
    print(cel)

choice = input("Would you like to convert from Celsius or Fahrenheit?")
if choice.title() == "Celsius":
    cel=int(input("Whats the temperature in Celsius?"))
    ctof(cel)
elif choice.title() == "Fahrenheit":
    fah=int(input("Whats the temperature in Fahrenheit"))
    ftoc(fah)
else:
    print("Try again")

    



