
def nth_prime(input):
    curr = 2
    cnt = 0
    primes = []

    while cnt != input:
        isPrime = True
        for p in primes:
            if curr % p == 0:
                isPrime = False
                break
        if isPrime:
            cnt += 1
            primes.append(curr)
            print(curr)

        curr += 1

    return primes.pop()


print(nth_prime(10001))
