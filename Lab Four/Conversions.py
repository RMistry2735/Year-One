def ctof(cel):
    fah = (cel * 1.8) + 32
    print(fah)

def ftoc(fah):
    cel = (fah - 32) / 1.8
    print(cel)


cel=int(input("Whats the temperature in Celsius?"))
ctof(cel)
fah=int(input("Whats the temperature in Fahrenheit"))
ftoc(fah)
