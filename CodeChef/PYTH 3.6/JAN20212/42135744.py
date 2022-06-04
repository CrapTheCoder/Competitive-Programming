for _ in range(int(input())):
    n = int(input())

    if n % 4 == 0: print(n)
    if n % 4 == 1: print(1)
    if n % 4 == 2: print(n+1)
    if n % 4 == 3: print(0)