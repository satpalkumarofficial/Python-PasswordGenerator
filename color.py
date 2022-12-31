Black = '\u001b[30m'
Red = '\u001b[31m'
Green = '\u001b[32m'
Yellow = '\u001b[33m'
Blue = '\u001b[34m'
Magenta = '\u001b[35m'
Cyan = '\u001b[36m'
White = '\u001b[37m'

Reset = '\u001b[0m'


def black(text):
    print(Black + text + Reset)


def red(text):
    print(Red + text + Reset)


def green(text):
    print(Green + text + Reset)


def yellow(text):
    print(Yellow + text + Reset)


def blue(text):
    print(Blue + text + Reset)


def magenta(text):
    print(Magenta + text + Reset)


def cyan(text):
    print(Cyan + text + Reset)


def white(text):
    print(White + text + Reset)
