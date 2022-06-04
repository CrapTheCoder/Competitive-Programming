for _ in range(int(input())):
    n = int(input())
    s = '*'

    for i in range(n):
        x = ' ' * ((n * 2 - 1 - len(s)) // 2)

        print(x + s + x)
        print(x + s + x)

        s = '*' + s + '*'