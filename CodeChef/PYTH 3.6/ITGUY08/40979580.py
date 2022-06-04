from collections import Counter

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split())) + list(map(int, input().split()))
    c = Counter(a)

    s = []
    for i in c:
        if c[i] == 1:
            s.append(i)

    print(*sorted(s))