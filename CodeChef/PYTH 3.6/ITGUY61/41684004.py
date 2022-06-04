for _ in range(int(input())):
    n = int(input())

    for i in range(n-1, 0, -1):
        print(' ' * (n-i-1) + '1' * (i*2+1))

    for i in range(n):
        print(' ' * (n-i-1) + '1' * (i*2+1))
