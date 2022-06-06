for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x, y, z = max(a, b, c) - a + 1, max(a, b, c) - b + 1, max(a, b, c) - c + 1
 
    if a == max(a, b, c) and b != max(a, b, c) and c != max(a, b, c): print(x-1, y, z); continue
    if a != max(a, b, c) and b == max(a, b, c) and c != max(a, b, c): print(x, y-1, z); continue
    if a != max(a, b, c) and b != max(a, b, c) and c == max(a, b, c): print(x, y, z-1); continue
    print(x, y, z)