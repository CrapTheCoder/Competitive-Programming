for _ in range(int(input())):
l, v, x, y = map(int, input().split())

print((l // v) - (y // v - (x - 1) // v))