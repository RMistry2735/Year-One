alpha = 'abcdefghijklmnopqrstuvxyz'

def ROT13(message):
    message = message.lower()
    encryptedmsg = ''
    for char in message:
        if char.isalpha():
            encryptedmsg += alpha[(alpha.index(char) + 13) % 26]
        else:
            encryptedmsg += char
    return encryptedmsg



message = input("Enter a message to encrypt")
print(ROT13(message))
