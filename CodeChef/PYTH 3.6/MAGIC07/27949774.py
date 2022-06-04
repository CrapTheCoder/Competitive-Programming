a = [0]

for i in range(1, 10 ** 6 + 5):
    c = 0

    if '7' in str(i) and '0' not in str(i):
        c = 1

    a.append(a[-1] + c)

for _ in range(int(input())):
    l, r = map(int, input().split())

    print(a[r] - a[l-1])
