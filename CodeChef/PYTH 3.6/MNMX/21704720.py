for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(min(a) * (n - 1))