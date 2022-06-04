from collections import Counter
from math import sqrt

def facts(n):
    if n % 2 == 0:
        yield 2

        while n % 2 == 0:
            n //= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            yield i

            while n % i == 0:
                n //= i

    if n > 2:
        yield n

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ms = [max(facts(i)) for i in a]

    cnt = Counter(ms)

    m = max(cnt.values())

    x = {i for i in ms if cnt[i] == m}

    print(max(x))