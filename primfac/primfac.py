import sys

def primfac(num):
    factorization = {}
    for i in range(2, num+1):
        while num % i == 0:
            num /= i*1.0
            if i in factorization:
                factorization[i] += 1
            else:
                factorization[i] = 1
        if num < i:
            break
    return factorization

if __name__ == "__main__":
    fact = primfac(int(sys.argv[1]))
    printstr = ""
    for prim in reversed(sorted(fact.keys())):
        for _ in range(fact[prim]):
            printstr += str(prim) + '*'
        #printstr += str(fact[prim]) + '*' + str(prim) + ' + '
    # print(printstr[:-3])
    print(printstr[:-1])
