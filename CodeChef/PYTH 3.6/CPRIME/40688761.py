def is_prime(n):
    return all(n % i for i in range(2, int(n ** 0.5) + 1)) and n >= 2

for _ in range(int(input())):
    n = input().strip()

    if is_prime(int(n)) and (n == n[::-1]):
        print('Yes')
    else:
        print('No')
