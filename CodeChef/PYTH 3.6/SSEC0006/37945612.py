def is_prime(n):
    return all(n % d for d in range(2, int(n ** 0.5) + 1)) and n >= 2

a = int(input())
b = int(input())

primes = []

for i in range(min(a, b), max(a, b) + 1):
    if is_prime(i):
        primes.append(i)

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if ((a/2) * (b/2)) <= primes[i] * primes[j] <= a*b:
            print(primes[i], primes[j], sep=',')