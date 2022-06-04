INF = float('inf')

def maxSubArraySum(a, n):
    m = -INF
    ml = 0

    for i in range(n):
        ml += a[i]
        if m < ml: m = ml
        if ml < 0: ml = 0

    return m

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(maxSubArraySum(a, n))