for _ in range(int(input())):
    n = int(input())

    if n == 0:
        print(1)
    else:
        i = 1
        while i < n:
            i *= 2

        if n == i or n == i-1:
            print(2 ** len(bin(n-1)[2:]))
        else:
            print(2 ** (len(bin(n-1)[2:]) - 1))
