for _ in range(int(input())):
    n, b = map(int, input().split())
    m = -1

    for _ in range(n):
        w, h, p = map(int, input().split())

        if w * h > m and p <= b:
            m = w * h

    print(m if m != -1 else 'no tablet')
