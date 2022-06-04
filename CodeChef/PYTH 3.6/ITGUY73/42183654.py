for _ in range(int(input())):
    n = int(input())
    s = list(range(1, n+1))

    for i in range(n):
        s.pop()
        print(*s, end='', sep='')
        print('*' * (2*i+1), end='', sep='')
        print(*s[::-1], sep='')
