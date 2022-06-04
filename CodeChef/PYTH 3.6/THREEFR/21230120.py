iv = lambda v: int(v)
sv = lambda v: str(v)
lv = lambda v: list(v)

li = lambda: list(map(int, input().split()))
mi = lambda: map(int, input().split())
ls = lambda: input().split()
ii = lambda: int(input())
si = lambda: input()

for _ in range(ii()):
    x, y, z = mi()

    combs = ((-x, y, z), (x, -y, z), (x, y, -z),
         (-x, -y, z), (-x, y, -z), (x, -y, -z),
         (-x, -y, -z))

    a = b = c = 10

    for i, j, k in combs:
        if sum([i, j, k]) == 0:
            print('yes')
            break
    else:
        print('no')
