n, q = map(int, input().split())
l = list(map(int, input().split()))
x, y = min(l), max(l)

for i in range(q):
    n = int(input())
    print('Yes' if x <= n <= y else 'No')