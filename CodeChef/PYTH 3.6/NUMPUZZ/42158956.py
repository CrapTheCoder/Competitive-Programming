def phi(n):
    result = n

    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p

            result *= (p-1) / p

        p += 1

    if n > 1:
        result *= (n-1) / n

    return int(result)

for _ in range(int(input())):
    n = int(input())
    print(phi(n))
