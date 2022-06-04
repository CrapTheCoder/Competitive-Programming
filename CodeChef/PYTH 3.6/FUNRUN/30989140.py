from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if max(a) != max(b):
        print('YES')
    else:
        print('NO')