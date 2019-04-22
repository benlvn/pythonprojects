import random

if __name__ == "__main__":
    while True:
        num1 = random.randint(1,99)
        num2 = random.randint(1,99)
        print(num1)
        print(num2, "+")
        ans = int(input())
        if ans != num1+num2:
            break
        print()
