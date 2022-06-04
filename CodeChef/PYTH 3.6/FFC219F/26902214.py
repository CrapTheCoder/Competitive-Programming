for _ in range(int(input())):
    n, p = map(int, input().split())
    a = sorted(map(int, input().split()))

    for i in range(n):
        p -= a[i]

        if p <= 0:
            print(i)
            break
    else:
        print(n)
