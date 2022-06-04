from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    c = int(input())

    if c == 0:
        print(2)
        print(1, 1)

    else:
        b = bin(c)[2:][::-1]
        ex = []

        for i in range(len(b)):
            if b[i] == '1':
                if i-1 >= 0 and b[i-1] == '1':
                    ex.pop()
                    ex.append(2 ** (i + 1) - 1)
                else:
                    if i != 0:
                        ex.append(2 ** i - 1)
                    ex.append(2 ** (i + 1) - 1)

        print(len(ex))
        print(*ex)