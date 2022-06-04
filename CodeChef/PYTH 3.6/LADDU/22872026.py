for _ in range(int(input())):
    n, o = input().split()
    s, n = 0, int(n)

    for i in range(int(n)):
        z = list(input().split())

        if z[0] == 'CONTEST_HOSTED': s += 50
        if z[0] == 'BUG_FOUND': s += int(z[1])
        if z[0] == 'TOP_CONTRIBUTOR': s += 300
        if z[0] == 'CONTEST_WON': s += 300 + max(0, 20 - int(z[1]))

    print(s // [200, 400][o != 'INDIAN'])