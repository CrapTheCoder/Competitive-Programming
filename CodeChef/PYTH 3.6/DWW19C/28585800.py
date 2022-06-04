from collections import Counter

for _ in range(int(input())):
    a = input()
    b = input()

    ac = Counter(a)
    bc = Counter(b)

    print(sum(k for k in (bc - ac).values() if k > 0))