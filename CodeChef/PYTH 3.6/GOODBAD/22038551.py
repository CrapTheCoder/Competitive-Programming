for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())

    a = sum(ord('a') <= ord(c) <= ord('z') for c in s)
    b = sum(ord('A') <= ord(c) <= ord('Z') for c in s)

    x = a <= k
    y = b <= k

    if x and y: print('both')
    elif x and not y: print('brother')
    elif not x and y: print('chef')
    elif not x and not y: print('none')
