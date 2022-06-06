for _ in range(int(input())):
    input()
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())
 
    if ((xa == xb == xf) and (min(ya, yb) <= yf <= max(ya, yb))) or ((ya == yb == yf) and (min(xa, xb) <= xf <= max(xa, xb))):
        print(abs(xa - xb) + abs(ya - yb) + 2)
    else:
        print(abs(xa - xb) + abs(ya - yb))