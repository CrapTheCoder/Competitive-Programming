for _ in range(int(input())):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))

    print(sum(not (i + k) % 7 for i in m))