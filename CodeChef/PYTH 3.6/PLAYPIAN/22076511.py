for _ in range(int(input())):
    s = input()

    print(['no', 'yes'][all(i + j in ['AB', 'BA'] for i, j in zip(s[::2], s[1::2]))])