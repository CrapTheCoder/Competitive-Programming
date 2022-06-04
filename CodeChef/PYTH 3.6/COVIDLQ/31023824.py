INF = float('inf')

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    last = -INF

    for i in range(n):
        if a[i] == 1:
            if i - last < 6:
                print('NO')
                break

            last = i
    else:
        print('YES')