for _ in range(int(input())):
    n = int(input())
    for i in range(10 ** (n-1), 10 ** n):
        if '0' in str(i):
            continue
        print(i)
