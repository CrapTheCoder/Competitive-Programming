for _ in range(int(input())):
    n = int(input())

    x = bin(n)[2:]

    print(int(x[1:] + x[0], 2))