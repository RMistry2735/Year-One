def factors(num):
    print("The factors of", num, "are;")
    for i in range(1 , num + 1):
        if num % i == 0:
            print(i)

factors(num = int(input("Enter a positive number")))
