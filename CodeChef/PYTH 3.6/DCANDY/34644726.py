for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))[::-1]
    print(sum(a[2::3]))