for _ in range(int(input())):
    n, x = map(int, input().split())
    s = input()

    v = set()
    v.add(x)

    for i in s:
        if i == 'L': x -= 1
        if i == 'R': x += 1

        v.add(x)

    print(len(v))