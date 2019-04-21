from sys import argv

def fib(num, mode):
    if mode == 1:
        if num == 1 or num == 2:
            return 1
        a = 1; b = 1
        for _ in range(num - 2):
            c = a + b; a = b; b = c;
        return c
    elif mode == 2:
        a = 1; b = 1
        while b < num:
            c = a + b; a = b; b = c
        return b

if __name__ == "__main__":
    if '1' == argv[1]:
        print(fib(int(argv[2]), 1))
    elif '2' == argv[1]:
        print(fib(int(argv[2]), 2))
