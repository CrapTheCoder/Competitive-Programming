for _ in range(int(input())):
    n = int(input())

    b = bin(n)[2:][::-1]

    s = 0

    for i in range(len(b)):
        if b[i] == '1':
            s += i

    print(s)