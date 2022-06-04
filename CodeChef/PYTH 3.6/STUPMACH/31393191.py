for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = 0
    m = float('inf')

    for i in a:
        m = min(m, i)

        s += m

    print(s)
