for _ in range(int(input())):
    n, k = map(int, input().split())
    remaining = 100 - k

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    defender = float('inf')
    forward = float('inf')

    for i in range(n):
        if b[i] == 0:
            defender = min(defender, a[i])

        if b[i] == 1:
            forward = min(forward, a[i])

    remaining -= defender + forward

    if 0 <= remaining:
        print('yes')
    else:
        print('no')