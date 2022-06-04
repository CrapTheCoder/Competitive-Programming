for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    b = [0] * 35

    for i in a:
        for j, l in enumerate(bin(i)[2:][::-1]):
            if l == '1':
                b[j] += 1

    s = 0
    for i in b:
        s += -(-i // k)

    print(s)