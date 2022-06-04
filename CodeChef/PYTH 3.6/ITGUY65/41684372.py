for _ in range(int(input())):
    n = int(input())

    for i in range(1, n+1):
        print(' ' * (n-i), end='')
        print(*range(1, i+1))