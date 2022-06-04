for _ in range(int(input())):
    a = sorted(map(int, input().split()))

    print(a[-1] if len(a) - 1 != a[-1] else a[-2])