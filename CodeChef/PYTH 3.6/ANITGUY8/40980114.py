from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    c = Counter(a)

    x = []
    for i in c:
        if c[i] > k:
            x.append(i)

    print(*sorted(x))