for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(sorted(a).index(a[int(input()) - 1]) + 1)