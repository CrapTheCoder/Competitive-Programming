from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    
    if x == y:
        if a == b:
            print('YES')
        else:
            print('NO')
        
        continue

    if abs(a - b) % abs(x - y) == 0:
        print('YES')
    else:
        print('NO')
