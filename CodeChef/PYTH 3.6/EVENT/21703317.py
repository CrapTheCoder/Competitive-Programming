days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for _ in range(int(input())):
    s, e, l, r = input().split()
    l, r = int(l), int(r)

    a = days.index(s) + 1
    b = days.index(e) + 1

    d = abs(b - a) + 1

    if a > b:
        d = 7 - a + b + 1

    i, c, ans = d, 0, 0

    while i <= 100:
        if l <= i <= r:
            c += 1
            ans = i

        i += 7

    if c == 0:
        print('impossible')
    elif c > 1:
        print("many")
    elif c == 1:
        print(ans)
