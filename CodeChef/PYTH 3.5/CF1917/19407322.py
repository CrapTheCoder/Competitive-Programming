for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))

    o = [i for i in a if i % 2]
    e = [i for i in a if not i % 2]

    if len(o) >= len(e):
        print('Petr')
    else:
        print('tourist')