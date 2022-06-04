t = int(input())

for i in range(t):
    xp = 0
    yp = 0

    m, n = map(int,input().split())
    x, y = map(int,input().split())
    l = int(input())
    s = input()

    xp += s.count('R')
    xp -= s.count('L')
    yp += s.count('U')
    yp -= s.count('D')

    print("Case " + str(i + 1), end= ': ', flush=True)
    if xp == x and yp == y:
        print("REACHED")

    elif xp < 0 or yp < 0 or xp > m or yp > n:
        print("DANGER")

    else:
        print("SOMEWHERE")