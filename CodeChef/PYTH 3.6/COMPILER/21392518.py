for _ in range(int(input())):
    string = input()
    ans = cur = 0

    for i, j in enumerate(string):
        if j == '<':
            cur += 1
        if j == '>':
            cur -= 1

            if not cur:
                ans = i + 1

        if cur < 0:
            break

    print(ans)