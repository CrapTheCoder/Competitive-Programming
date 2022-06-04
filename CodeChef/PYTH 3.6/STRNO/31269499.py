from math import sqrt

def facts(n):
    while n % 2 == 0:
        yield 2
        n = n // 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            yield i
            n = n // i

    if n > 2:
        yield n


for _ in range(int(input())):
    x, k = map(int, input().split())

    if len(list(facts(x))) >= k:
        print(1)
    else:
        print(0)
