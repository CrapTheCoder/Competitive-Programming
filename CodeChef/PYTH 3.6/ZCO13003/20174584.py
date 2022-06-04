n, k = map(int, input().split())
arr = sorted(map(int, input().split()))

l = 0
r = n - 1
result = 0

while l < r:
    if arr[l] + arr[r] < k:
        result += r - l
        l += 1
    else:
        r -= 1

print(result)