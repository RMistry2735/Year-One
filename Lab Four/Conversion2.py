def ctof(cel):
    fah = (cel * 1.8) + 32
    print("The temperature is", fah,"°F")

cel=int(input("Whats the temperature in Celsius?"))
ctof(cel)
