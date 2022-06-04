def add(l, h):
    a[l] += 1

    if h != n - 1:
        a[h + 1] -= 1

def update():
    for i in range(1, n):
        a[i] += a[i-1]

for _ in range(int(input())):
    n = int(input())

    c = list(map(int, input().split()))
    h = list(map(int, input().split()))

    a = [0] * n

    for i in range(n):
        add(max(0, i-c[i]), min(i+c[i], n-1))

    update()

    print(['NO', 'YES'][sorted(a) == sorted(h)])