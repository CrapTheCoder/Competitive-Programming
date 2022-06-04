for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(sum((i-1) % 6 + 1 for i in a))