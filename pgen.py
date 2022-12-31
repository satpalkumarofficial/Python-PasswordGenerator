import random
import color as cprint

Nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
Alps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Syms = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '_', '-', '+', '=', '/', '*', '|', '}', '{',
        ']', '[', '>', '<', ',', '.', ';', ':', '"']
choices = [Nums, Alps, alps, Syms]


def generateRandomPassword():
    characters = []
    characters.append(random.choice(Alps))
    characters.append(random.choice(alps))
    characters.append(random.choice(Syms))
    characters.append(random.choice(Nums))
    characters.append(random.choice(Alps))
    characters.append(random.choice(alps))
    characters.append(random.choice(Syms))
    characters.append(random.choice(Nums))
    characters.append(random.choice(Alps))
    characters.append(random.choice(alps))
    characters.append(random.choice(Syms))
    characters.append(random.choice(Nums))
    password = ''.join(characters)
    return password


def generateNamedPassword(name):
    password = ''
    if (len(name) == 3):
        characters = []
        characters.append(random.choice(random.choice(choices)))
        characters.append(name)
        characters.append(random.choice(Syms))
        characters.append(random.choice(Alps))
        characters.append(random.choice(random.choice(choices)))
        characters.append(random.choice(random.choice(choices)))
        characters.append(random.choice(alps))
        characters.append(random.choice(Nums))
        password = ''.join(characters)

    elif (len(name) == 4):
        characters = []
        characters.append(random.choice(random.choice(choices)))
        characters.append(name)
        characters.append(random.choice(Syms))
        characters.append(random.choice(Alps))
        characters.append(random.choice(random.choice(choices)))
        characters.append(random.choice(alps))
        characters.append(random.choice(Nums))
        password = ''.join(characters)

    elif (len(name) == 5):
        characters = []
        characters.append(random.choice(random.choice(choices)))
        characters.append(name)
        characters.append(random.choice(Syms))
        characters.append(random.choice(Alps))
        characters.append(random.choice(alps))
        characters.append(random.choice(Nums))
        password = ''.join(characters)

    elif (len(name) > 5):
        characters = []
        characters.append(random.choice(random.choice(choices)))
        characters.append(name[:5])
        characters.append(random.choice(Syms))
        characters.append(random.choice(Alps))
        characters.append(random.choice(alps))
        characters.append(random.choice(Nums))
        password = ''.join(characters)

    return password


def genListOfRandomPass():
    cprint.blue('Your Generated Password:\n')
    for x in range(0, 10):
        cprint.green(generateRandomPassword() + '\n')
        # print(generateRandomPassword() + '\n')


def genListOfNamedPass():
    name = input('Enter your name: ')
    cprint.blue('Your Generated Password:\n')
    for y in range(0, 10):
        cprint.green(generateNamedPassword(name) + '\n')


genListOfRandomPass()
genListOfNamedPass()
