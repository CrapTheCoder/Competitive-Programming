from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    c = Counter(s)

    odd = 0
    for i in c:
        if c[i] % 2:
            odd += 1

    if odd > 1:
        print(odd - 1)
    else:
        print(0)