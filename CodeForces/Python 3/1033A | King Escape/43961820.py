n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
 
pos = ((ax < bx) == (ax < cx)) and ((ay < by) == (ay < cy))
 
print('YES' if pos else 'NO')