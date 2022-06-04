for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(k):
        a[i::k] = sorted(a[i::k])

    if sorted(a) == a:
        print('yes')
    else:
        print('no')