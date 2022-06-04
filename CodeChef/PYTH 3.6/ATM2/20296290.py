for _ in range(int(input())):
    n, i = map(int, input().split())
    a = list(map(int, input().split()))

    r = ''

    for x in a:
        if x <= i:
            r += '1'
            i -= x
        else:
            r += '0'

    print(r)