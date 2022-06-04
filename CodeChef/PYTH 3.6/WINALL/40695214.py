def is_prime(n):
    return all(n % i for i in range(2, int(n ** 0.5) + 1)) and n >= 2

for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print('Grinch')
        continue

    if n == 2 or n % 2:
        print('Me')
        continue

    if not (n & (n-1)):
        print('Grinch')
        continue

    if is_prime(n // 2):
        print('Grinch')
        continue

    print('Me')
