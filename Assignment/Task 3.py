import re
import random

stdntNo = []
stdnt_name = []
emails = []

if __name__ == "__main__":

    f0 = open("Students.txt", 'r')
    f1 = open("email.txt", 'a')

    for line in f0:
        stdntNo.append(line[0:7])
        stdnt_name.append(line[9:].split(", "))

    for name in stdnt_name:
        name[1] = name[1].strip()
        name[0] = re.sub(r'[^a-zA-Z\s]', '', name[0])
        only_upper = '.'.join(char for char in name[1] if char.isupper())
        number = random.randint(1000, 9999)
        emails.append(only_upper.lower() + '.' + name[0].lower() + str(number) + '@poppleton.ac.uk\n')

    for number, email in zip(stdntNo, emails):
        f1.write(f"{number} {email}")

    f1.close()
    f0.close()
    print("Process completed successfully")

