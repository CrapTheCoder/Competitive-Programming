import sys
sys.setrecursionlimit(1000000000)

def minutes(i = 0, f = 0):
    if f == 3: return float('inf')
    if i == n: return 0
    if arr[i][f] != -1: return arr[i][f]

    arr[i][f] = min(a[i] + minutes(i + 1), minutes(i + 1, f + 1))
    return arr[i][f]

n = int(input())
a = list(map(int, input().split()))

arr = [[-1 for __ in range(3)] for _ in range(n)]

print(minutes())