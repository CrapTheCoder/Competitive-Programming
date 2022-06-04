for _ in range(int(input())):
    l = list(map(int, input().split()))
    print(['Champions', -1][max(l) != l[0]])
