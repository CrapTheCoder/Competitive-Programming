for _ in range(int(input())):
    n = int(input())

    print('1' * n)

    s = list(' ' * n)
    s[0] = s[-1] = '1'

    l, r = 1, n-2
    for i in range(2, n):
        s[l] = s[r] = '1'
        print(*s, sep='')
        s[l] = s[r] = ' '

        l += 1
        r -= 1

    if n != 1:
        print('1' * n)