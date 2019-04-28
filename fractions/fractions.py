class Fractions:

    def __init__(self, numerator, denomenator):
        self.numerator = numerator
        self.denomenator = denomenator

    def print(self):
        return str(self.numerator) + '/' + str(self.denomenator)

    def reduce(self):
        igcd = None
        if self.numerator > self.denomenator:
            igcd = gcd(self.denomenator, self.numerator)
        else:
            igcd = gcd(self.numerator, self.denomenator)
        self.numerator /= igcd
        self.denomenator /= igcd

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
