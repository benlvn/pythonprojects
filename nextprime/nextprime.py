def make_sieve(n):
    sieve = [True]*n
    sieve[0] = False
    sieve[1] = False
    for i in range(n):
        if sieve[i]:
            sieve[2*i::i] = [False]*len(sieve[2*i::i])
    return sieve

if __name__ == "__main__":
    sieve = make_sieve(1000000)
    for i in range(len(sieve)):
        if sieve[i]:
            print(i, end="")
            i = input()
