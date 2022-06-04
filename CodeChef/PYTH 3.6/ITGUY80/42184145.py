for _ in range(int(input())):
    n = int(input())
    s = ['*'] * n

    for i in range(n):
        l = [i+1]
        c = n-1

        for j in range(i):
            l.append(l[-1] + c)
            c -= 1

        print(*(l+['*']), sep='')