from sys import argv
import csv
from random import randint

class AppInstance:

    def __init__(self, filename):
        self.flashdict = self.interpret_csv(filename)
        self.numcards = len(self.flashdict)
        self.correct_guesses = 0
        self.unguessed = list(self.flashdict.keys())
        self.current_card = None
        self.running = True
    
    def interpret_csv(self, filename):
        translation_dict = {}
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                translation_dict[row[0]] = row[1]
        return translation_dict

    def pop_random(self):
        randind = randint(0, len(self.unguessed)-1)
        self.current_card = self.unguessed[randind]
        self.unguessed = self.unguessed[:randind] + self.unguessed[randind+1:]

    def show_card(self):
        self.pop_random()
        return self.current_card

    def make_guess(self, guess):
        if guess == self.flashdict[self.current_card]:
            self.correct_guesses += 1
        if len(self.unguessed) == 0:
            self.running = False


if __name__ == "__main__":
    inst = AppInstance('easyflash.txt')
    while inst.running:
        print(inst.show_card())
        inst.make_guess(input("> "))
    correct = inst.correct_guesses
    outof = inst.numcards
    print("Score: " + str(correct) + '/' + str(outof))
    print(str(float(correct)/float(outof)*100))

