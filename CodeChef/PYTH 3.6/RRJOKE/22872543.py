for _ in range(int(input())):
    n = int(input())
    r = 0

    for i in range(n):
        input()
        r = r ^ (i+1)

    print(r)
