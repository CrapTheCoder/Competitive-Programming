for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(key=(lambda x: x % 2))
    b.sort(key=(lambda x: x % 2))

    c = 0

    for i in range(n):
        try:
            c += (a[i] + b[i]) // 2
        except:
            print(i)

    print(c)