for _ in range(int(input())):
    x, y = map(int, input().split())
    print(max(0, x-y))