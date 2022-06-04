for _ in range(int(input())):
    n, k = map(int, input().split())
    j = sorted(map(int, input().split()))

    print(sum(j[-k:]))
