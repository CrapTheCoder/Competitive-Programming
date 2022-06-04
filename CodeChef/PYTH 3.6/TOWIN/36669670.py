for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)

    if n == 1:
        print('first')
        continue

    x1 = a[0] + sum(a[3::2])
    x2 = a[1]

    if len(a) > 2:
        x2 += a[2] + sum(a[4::2])

    if x1 > x2:
        print('first')
    if x1 < x2:
        print('second')
    if x1 == x2:
        print('draw')
