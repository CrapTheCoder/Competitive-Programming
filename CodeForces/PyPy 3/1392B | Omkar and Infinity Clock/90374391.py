for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = [min(a), max(a)][k % 2]
    print(*[abs(i - m) for i in a])