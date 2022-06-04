from math import sqrt

for _ in range(int(input())):
    a, b, g = map(float, input().split())
    l, n = map(int, input().split())

    f = [[2, 0]]

    for _ in range(n):
        f.append(list(map(int, input().split())))

    f.sort(key=lambda x: x[-1])

    f.append([-1, l])

    ttim = tim = vel = 0

    try:
        for i in range(1, n+2):
            dis = f[i][1] - f[i-1][1]
            acc = -1

            if f[i-1][0] == 1: acc = -b
            if f[i-1][0] == 2: acc = a
            if f[i-1][0] == 3: acc = -g

            tim = (-vel + sqrt(2 * acc * dis + vel ** 2)) / acc
            vel = vel + acc * tim

            ttim += tim

        print(ttim)

    except:
        print(-1)