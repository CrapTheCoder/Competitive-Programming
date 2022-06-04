for _ in range(int(input())):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))

    d = {}

    for i in a:
        d[i] = d.get(i, 0) + 1

    for i in d.values():
        if i % 2 == 1:
            print('Gaitonde')
            break
    else:
        print('Isa')