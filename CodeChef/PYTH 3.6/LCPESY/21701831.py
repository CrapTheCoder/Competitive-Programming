from collections import Counter

for _ in range(int(input())):
    a = input()
    b = input()
    c = Counter(a) - Counter(b)

    s = sum(c.values())

    print(len(a) - s)