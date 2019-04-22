from sys import argv
import random

if __name__ == "__main__":
    boyfile = open('male-first-names.txt', 'r')
    girlfile = open('female-first-names.txt', 'r')
    boy_names = boyfile.read().split()
    girl_names = girlfile.read().split()
    resp = input()
    while resp != 'q':
        if resp == 'b':
            print(random.choice(boy_names).lower().capitalize())
        if resp == 'g':
            print(random.choice(girl_names).lower().capitalize())
        resp = input()
