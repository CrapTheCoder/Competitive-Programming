for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    print(2 ** sum(not i % m for i in a) - 1)
