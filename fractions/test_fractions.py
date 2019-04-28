import unittest
from fractions import Fractions

class TestFractions(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print('setUpClass')
        self.f1 = Fractions(5,7)
        self.f2 = Fractions(13,8)
        self.f3 = Fractions(21,27)

    def test_print(self):
        print('test_print')
        self.assertEqual(self.f1.print(), '5/7')
        self.assertEqual(self.f2.print(), '13/8')
        self.assertEqual(self.f3.print(), '21/27')

    def test_reduce(self):
        print('test_reduce')
        self.f1.reduce()
        self.f2.reduce()
        self.f3.reduce()
        self.assertEqual(self.f1.numerator, 5)
        self.assertEqual(self.f1.denomenator, 7)
        self.assertEqual(self.f2.numerator, 13)
        self.assertEqual(self.f2.denomenator, 8)
        self.assertEqual(self.f3.numerator, 7)
        self.assertEqual(self.f3.denomenator, 9)
    

if __name__ == '__main__':
    unittest.main()
