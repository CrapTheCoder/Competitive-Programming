for _ in range(int(input())):
    n, q = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    m = 1

    for i in d: m *= i
    for h, i in enumerate(a): a[h] = str(i // m)

    print(' '.join(a))