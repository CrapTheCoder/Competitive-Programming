for _ in range(int(input())):
    n = int(input())
    s = ['*'] * n

    for i in range(n):
        s[i] = (i+1)
        print(*s, sep='')