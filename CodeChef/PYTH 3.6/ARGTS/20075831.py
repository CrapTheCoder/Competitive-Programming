t, k = map(int, input().split())

f = 'FAILURE'
s = 'SUCCESS'

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    a = sum(arr[:n])
    print(f if a > k else s)
