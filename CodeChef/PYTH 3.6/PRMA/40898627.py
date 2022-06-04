n = int(input())
a = list(map(int, input().split()))

l = 1
while l < n:
    if a[l-1] != l:
        break
    l += 1

r = n
while r >= 0:
    if a[r-1] != r:
        break
    r -= 1

if l > r:
    print(0, 0)
    exit()

a[l-1:r] = a[l-1:r][::-1]

if a == list(range(1, n+1)):
    print(l, r)
else:
    print(0, 0)
