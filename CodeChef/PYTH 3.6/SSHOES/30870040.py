from collections import Counter

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    c = Counter(s)

    for i in c:
        if not (c[i] % 2 == 0 and c[i] // 2 <= k):
            print('NO')
            break
    else:
        print('YES')
