for _ in range(int(input())):
    a, b, l, r = map(int, input().split())

    x = r // (a + b)
    rc = x * 2
    if x * (a + b) + a <= r:
        rc += 1

    if l == 0:
        print(rc)
        continue

    l -= 1
    y = l // (a + b)
    lc = y * 2
    if y * (a + b) + a <= l:
        lc += 1

    print(rc - lc)
