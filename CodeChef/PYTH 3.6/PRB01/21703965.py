def isPrime(p):
    return all(p % i for i in range(2, int(p ** 0.5))) and p > 1

for _ in range(int(input())):
    print('yes' if isPrime(int(input())) else 'no')