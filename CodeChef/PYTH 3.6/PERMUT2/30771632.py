from sys import stdin
input = stdin.readline

while True:
    if input() == '0\n':
        break

    a = list(map(int, input().split()))
    inv = [-1] * len(a)

    for i, j in enumerate(a):
        inv[j-1] = i+1

    print('ambiguous' if inv == a else 'not ambiguous')
