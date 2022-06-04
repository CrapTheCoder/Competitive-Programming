for _ in range(int(input())):
    n = int(input())
    p = input()

    sa = ma = sb = mb = 0

    for i in range(2 * n):
        if i % 2:
            if p[i] == '1':
                sb += 1
            else:
                mb += 1
        else:
            if p[i] == '1':
                sa += 1
            else:
                ma += 1

        if sa + mb == n + 1 or sb + ma == n + 1:
            print(i + 1)
            break

    else:
        print(2 * n)