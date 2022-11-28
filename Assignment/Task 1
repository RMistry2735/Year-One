import random
List = ["Goat", "Aardvark", "Albatross", "Anaconda", "Ape", "Armadillo", "Baboon","Barnacle", "Bonobo", "Butterfly", "Camel", "Capybara", "Cardinal", "Carp", "Catshark", "Caterpillar",
        "Catfish", "Centipede", "Chameleon", "Cheetah", "Chickadee", "Chicken", "Chimpanzee", "Chipmunk", "Clownfish", "Cobra", "Cockroach", "Constrictor", "Cougar", "Coyote", "Crab", "Crayfish",
        "Cricket", "Crocodile", "Cuckoo", "Cicada", "Dinosaur", "Dolphin", "Dragonfly", "Eagle", "Elephant", "Falcon", "Flamingo", "Fowl" ]

while True:
    try:
        Passcount = int(input("How many passwords do you want to generate? "))
        if  Passcount < 1:
            print("Please enter a value between 1 and 24. ")
        elif Passcount > 24:
            print("Please enter a value between 1 and 24. ")
        else:
            print("Generating Passwords. ")
            break
    except ValueError:
        print("Please Enter a value")


for number in range(Passcount):

    Word1 = random.choice(List)
    Word2 = random.choice(List)
    Word3 = random.choice(List)

    Password = (Word1 + Word2 + Word3)
    print(Password)
