def remlast(text):
    if len(text) <= 1:
        print(text)
    else:
        rmtext = text.rstrip(text[-1])
        print(rmtext)

text = input("Enter a message")
remlast(text)
