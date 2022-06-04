for _ in range(int(input())):
    a = input()
    b = input()

    n = len(a)
    m = len(b)

    if n == m == 1:
        print('Yes' if a == b else 'No')
    else:
        s = set(a).intersection(set(b))
        print('Yes' if s else 'No')