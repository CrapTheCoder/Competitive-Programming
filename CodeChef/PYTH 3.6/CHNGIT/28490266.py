from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = input().split()

    c = Counter(a)

    print(n - max(c.values()))
