from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))

    if b[-1] > a[-1]:
        x = b[-1] - a[-1]
        c = [i-x for i in b]

        d1 = Counter(a)
        d2 = Counter(c)

        for i in d2:
            if d1[i] - d2[i] < 0:
                break

        else:
            print(x)
            continue

    x = b[-1] - a[-2]
    print(x)
