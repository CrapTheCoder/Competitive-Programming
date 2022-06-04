from math import sqrt, floor, ceil

def solve(l, r):
    return floor(sqrt(r)) - ceil(sqrt(l)) + 1

for _ in range(int(input())):
    l, r = sorted(map(int, input().split()))

    print(r - l + 1 - solve(l, r))