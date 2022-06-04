from copy import deepcopy

def rotate(a, n):
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = a[i][j]
            a[i][j] = a[j][n - 1 - i]
            a[j][n - 1 - i] = a[n - 1 - i][n - 1 - j]
            a[n - 1 - i][n - 1 - j] = a[n - 1 - j][i]
            a[n - 1 - j][i] = temp

def display(a):
    print(*(' '.join(str(j) for j in i) for i in a), sep='\n')

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = [list(map(int, input().split())) for __ in range(n)]
    b = deepcopy(a)
    rotate(b, n)
    c = [i[::-1] for i in a[::-1]]
    d = deepcopy(a)
    rotate(d, n)
    rotate(d, n)
    rotate(d, n)

    l = [a, b, c, d]

    m = 0

    for __ in range(q):
        x, n = input().split()
        n = int(n)

        if x == 'R':
            n = (-n) % 4

        m = m + n

    display(l[m % 4])

