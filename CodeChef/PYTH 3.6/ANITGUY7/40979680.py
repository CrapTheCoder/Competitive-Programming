from collections import Counter

for _ in range(int(input())):
    input()
    a = sorted(map(int, input().split()))

    print(a[-1] * a[-2], a[0] * a[1])