for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    last = 0

    i = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            last = i
            break

    if last == 0:
        print('YES')
        print(0)
        continue

    if a[last:] + a[:last] == sorted(a):
        print('YES')
        print(1)
        continue

    print('NO')
