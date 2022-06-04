for _ in range(int(input())):
    n = int(input())

    for i in range(1, n//2+2):
        print(((str(i) + '*') * i)[:-1])

    for i in range(n//2, 0, -1):
        print(((str(i) + '*') * i)[:-1])
