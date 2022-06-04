import sys
sys.setrecursionlimit(1000000000)

def money(i = 0, f = 0):
    if f == 3: return float('-inf')
    if i == n: return 0
    if arr[i][f] != -1: return arr[i][f]

    x = money(i + 1)
    y = money(i + 1, f + 1)

    arr[i][f] = max(x, a[i] + y)
    return arr[i][f]



n = int(input().strip())
a = list(map(int, input().split()))

arr = [[-1 for __ in range(3)] for _ in range(n)]

print(money())