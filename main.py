import random as rand

acceptableCharacters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'x', 'y', 'z',
                        '1', '2', '3', '4', '5', '6', '7', '8', '9']

specialCharacters = ['!', '@', '#', '$', '%',
                     '^', '&', '*', '+', '-', '/', '<', '>', '?']

passwordLength = int(input("What's the length of the password? "))
hasSpecialChars = True if input("do you want special characters? (Y/N) ") == 'Y' else False
password = ""
for i in range(passwordLength):
    char = acceptableCharacters[rand.randrange(len(acceptableCharacters))]
    isUpper = rand.randrange(3)
    if isUpper % 3 == 0:
       char = char.upper()
    password += char

if(hasSpecialChars):
    nbSpecChars = rand.randrange(passwordLength//2)
    for i in range(nbSpecChars):
        j = rand.randrange(len(password))
        password = list(password)
        password[j] = specialCharacters[rand.randrange(len(specialCharacters))]

password = ''.join(password)
print(password)
