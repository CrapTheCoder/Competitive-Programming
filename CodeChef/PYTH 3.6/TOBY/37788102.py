from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = input()
    c = Counter(s)

    print(min(c['L'], c['R']) * 2 + min(c['U'], c['D']) * 2)
