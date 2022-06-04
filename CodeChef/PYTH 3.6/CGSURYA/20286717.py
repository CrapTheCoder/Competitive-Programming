def maxSub(a):
    m = float('-inf')
    ma = 0

    for i in range(len(a)):
        ma = ma + a[i]
        if m < ma:
            m = ma

        if ma < 0:
            ma = 0
    return m

for _ in range(int(input())):
    n = int(input())

    p = input()
    a = list(map(int, input().split()))

    for i in range(n):
        if p[i] == 'L':
            a[i] *= -1

    print(maxSub(a))