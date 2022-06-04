for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        if i % 2 == 0:
            print('*' * (i+1))
        else:
            print('?' * (i + 1))