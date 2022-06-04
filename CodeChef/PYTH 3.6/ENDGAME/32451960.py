for _ in range(int(input())):
    r, c = map(int, input().split())
    x, y = map(int, input().split())

    print(max(
        max(abs(x - 0), abs(y - 0)),
        max(abs(x - 0), abs(y - c+1)),
        max(abs(x - r+1), abs(y - 0)),
        max(abs(x - r+1), abs(y - c+1)),
    ))
