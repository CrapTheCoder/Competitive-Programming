for _ in range(int(input())):
    n = int(input())
    l = [int(input()) for i in range(n)]

    print(f'Case {_ + 1}:')
    print(*[i & 2 ** 16 - 1 for i in l])
    print(*[(i & (2 ** 32 - 2 ** 16)) // 2 ** 16 for i in l])