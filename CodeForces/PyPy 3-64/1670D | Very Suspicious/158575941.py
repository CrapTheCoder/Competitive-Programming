from sys import stdin
input = stdin.readline
 
from math import ceil
for _ in range(int(input())):
    n = int(input())
    print(ceil((n*3 / 2) ** 0.5))