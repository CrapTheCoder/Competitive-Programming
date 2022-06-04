for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    r = list(range(1, n // 2 + 1))
    b = r + [n // 2 + 1] + r[::-1]

    print('yes' if a == b else 'no')