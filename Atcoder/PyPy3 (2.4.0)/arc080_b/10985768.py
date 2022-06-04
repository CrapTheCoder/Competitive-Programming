h, w = map(int, input().split())

n = int(input())
a = list(map(int, input().split()))

g = [[-1] * w for _ in range(h)]

ch = 0
cw = 0
o = 1

for i in range(n):
    while a[i] > 0:
        g[ch][cw] = i + 1

        a[i] -= 1

        if not (0 <= cw + o < w):
            ch += 1

            if o == 1:
                o = -1
            else:
                o = 1
        else:
            cw += o

for i in g:
    print(*i)
