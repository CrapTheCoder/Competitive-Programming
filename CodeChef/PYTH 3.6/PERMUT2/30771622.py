from sys import stdin
input = stdin.readline

while True:
    n = int(input())

    if n == 0:
        break

    a = list(map(int, input().split()))
    inv = [-1] * n

    for i in range(n):
        inv[a[i]-1] = i+1

    print('ambiguous' if inv == a else 'not ambiguous')