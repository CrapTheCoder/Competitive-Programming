for _ in range(int(input())):
    s = list(input())
    c = m = 0
    for i in s:
        if i == '(': c += 1
        if i == ')': c -= 1

        m = max(c, m)

    print('(' * m + ')' * m)