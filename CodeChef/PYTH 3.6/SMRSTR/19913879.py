for _ in range(int(input())):
    n, q = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    m = 1

    for i in d:
        m *= i

    lis = []

    for i in a:
        lis.append(str(i // m))
    print(' '.join(lis))