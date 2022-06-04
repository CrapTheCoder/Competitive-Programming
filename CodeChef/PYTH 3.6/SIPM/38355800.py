for _ in range(int(input())):
    n = int(input())
    a = set(map(int, input().split()))

    print(sum(i for i in a if i > 0), sum(i for i in a if i < 0))
