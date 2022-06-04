for _ in range(int(input())):
    n, k, e, m = map(int, input().split())

    a = [sum(list(map(int, input().split()))) for i in range(n)]
    l, a = a[-1], sorted(a[:-1], reverse=True)
    r = max(a[k-1] - l + 1, 0)

    if r <= m: print(r)
    else: print('Impossible')
