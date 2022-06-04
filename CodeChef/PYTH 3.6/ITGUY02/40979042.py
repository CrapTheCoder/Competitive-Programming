for _ in range(int(input())):
    n = int(input())

    x = (n * 2 - 1)
    l = [' '] * x
    a, b = x // 2, x // 2

    l[a] = '*'
    print(*l, sep='')

    for i in range(n-2):
        l[a] = l[b] = ' '

        a -= 1
        b += 1

        l[a] = l[b] = '*'
        print(*l, sep='')

    if n > 1:
        print(x * '*')