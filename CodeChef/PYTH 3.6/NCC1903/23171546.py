for _ in range(int(input())):
    n = int(input())
    k = int(input())
    a = sorted(map(int, input().split()))

    c = 0

    for i in a:
        n -= i

        if n < 0:
            break

        c += 1

    print(c)