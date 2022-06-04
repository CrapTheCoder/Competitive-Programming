for _ in range(int(input())):
    r = int(input())

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    d1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    d2 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    d3 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5

    e1 = 1 if d1 <= r else 0
    e2 = 1 if d2 <= r else 0
    e3 = 1 if d3 <= r else 0

    print('yes' if (e1 or (e2 and e3)) and (e2 or (e1 and e3)) and (e3 or (e1 and e2)) else 'no')