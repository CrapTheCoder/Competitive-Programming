from itertools import groupby


for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    l = [i[0] for i in groupby(s)]
    print(min(l.count('B'), l.count('W')))