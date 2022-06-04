for _ in range(int(input())):
    x, y, k = map(int, input().split())

    print(['Chef', 'Paja'][((x + y) // k) % 2])
