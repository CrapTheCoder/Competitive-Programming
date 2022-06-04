from sys import stdin

d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

input = stdin.readline

n = int(input())

tree = [[0] * n * 2 for _ in range(26)]

def build(arr):
    for i in range(n):
        tree[ddd][n + i] = arr[i]

    for i in range(n - 1, 0, -1):
        tree[ddd][i] = tree[ddd][i << 1] + tree[ddd][i << 1 | 1]

def update(p, value):
    p += n
    tree[ddd][p] = value

    i = p

    while i > 1:
        tree[ddd][i >> 1] = tree[ddd][i] + tree[ddd][i ^ 1]
        i >>= 1

def query(l, r):
    res = 0

    l += n
    r += n

    while l < r:

        if l & 1:
            res += tree[ddd][l]
            l += 1

        if r & 1:
            r -= 1
            res += tree[ddd][r]

        l >>= 1
        r >>= 1

    return res

s = list(input())

arrs = [[0] * n for _ in range(26)]

for i in range(n):
    arrs[d[s[i]]][i] = 1

for ddd in range(26):
    build(arrs[ddd])

for _ in range(int(input())):
    t = input().split()

    if t[0] == '1':
        i, c = t[1:]
        i = int(i) - 1

        new = d[c]
        cur = d[s[i]]

        s[i] = c

        ddd = cur
        update(i, 0)

        ddd = new
        update(i, 1)

    if t[0] == '2':
        l, r = map(int, t[1:])
        l -= 1
        r -= 1

        ans = 0

        for ddd in range(26):
            if query(l, r + 1) != 0:
                ans += 1

        print(ans)