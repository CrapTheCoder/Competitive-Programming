for _ in range(int(input())):
    n = int(input())
    b = bin(10 ** n - 1)[2:]
 
    x, y = divmod(n, 4)
    r = '8' * (x + int(y != 0))
 
    print((r + '9' * n)[:n][::-1])