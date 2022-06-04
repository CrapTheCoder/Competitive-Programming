for _ in range(int(input())):
    s = input()

    c = lc = 0

    for i, j in enumerate(s):
        if j == '<': c += 1
        if j == '>': c -= 1

        if c == 0:
            lc = i+1

        if c < 0:
            break

    print(lc)
