for _ in range(int(input())):
    r, c = map(int, input().split())
    x, y = map(int, input().split())

    print(max(
        abs(x - 0) + abs(y - 0),
        abs(x - 0) + abs(y - c+1),
        abs(x - r+1) + abs(y - 0),
        abs(x - r+1) + abs(y - c+1),
    ))
