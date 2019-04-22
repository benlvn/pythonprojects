from sys import argv
from math import sqrt, ceil

def tri(num, mode):
    if mode == 1:
        return int(num*(1+num)/2)
    elif mode == 2:
        n = ceil((-1+sqrt(1+8*num))/2)
        return tri(n, 1)

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python3 triangle_number [method] [num]")
        exit(1)
    if '1' == argv[1]:
        print(tri(int(argv[2]), 1))
    elif '2' == argv[1]:
        print(tri(int(argv[2]), 2))

