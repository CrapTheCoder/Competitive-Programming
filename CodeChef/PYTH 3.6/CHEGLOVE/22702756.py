for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    g = list(map(int, input().split()))

    f = all(l[i] <= g[i] for i in range(n))
    b = all(l[-i-1] <= g[i] for i in range(n))

    if f and b: ans = 'both'
    elif f and not b: ans = 'front'
    elif not f and b: ans = 'back'
    else: ans = 'none'

    print(ans)
