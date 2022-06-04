for _ in range(int(input())):
    n = int(input())

    l = list(map(int, input().split()))
    m = list(range(1, n+1))

    if (l == m) or (sorted(l) != m): print('no')
    else: print('yes')
