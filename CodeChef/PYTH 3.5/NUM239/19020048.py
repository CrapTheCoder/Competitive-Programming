for t in range(int(input())):
    ans = 0
    a, b = map(int, input().split())

    for i in range(a, b + 1):
        il = list(str(i))

        if il[-1] == '2' or il[-1] == '3' or il[-1] == '9':
            ans += 1

    print(ans)