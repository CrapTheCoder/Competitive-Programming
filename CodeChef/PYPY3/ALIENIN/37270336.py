LEFT = 0
RIGHT = 10 ** 16

def is_valid(x):
    # x = x / (10 ** 6)
    m = 0

    for i in a:
        if m < i:
            m = i

        if (i + d) - m < 0:
            return False

        m += x

    return True

def bins():
    l, r = LEFT, RIGHT

    while l < r:
        m = -(-(l + r) // 2)

        if is_valid(m):
            l = m
        else:
            r = m - 1

    return l

for _ in range(int(input())):
    n, d = map(int, input().split())
    d *= 10 ** 6
    a = sorted(map(lambda x: int(x) * 10 ** 6, input().split()))

    print('{:.10f}'.format(bins() / (10 ** 6)))
