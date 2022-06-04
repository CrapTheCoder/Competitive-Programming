for _ in range(int(input())):
    p, idx = map(int, input().split())

    b = bin(idx)[2:]

    print(int(('0' * (p - len(b)) + b)[::-1], 2))