from random import choice
from string import ascii_uppercase

if __name__ == "__main__":
    while True:
        print(choice(ascii_uppercase), end='')
        input()
