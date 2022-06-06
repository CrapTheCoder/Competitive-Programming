from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    x = list(map(int, input().strip()))
    for i in range(len(x) - 1, 0, -1):
        s = x[i-1] + x[i]
        if s > 9:
            x[i-1] = s // 10
            x[i] = s % 10
            print(*x, sep='')
            break
 
    else:
        x = [x[0] + x[1]] + x[2:]
        print(*x, sep='')