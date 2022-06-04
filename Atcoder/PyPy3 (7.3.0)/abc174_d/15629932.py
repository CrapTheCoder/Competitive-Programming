n = int(input())
a = list(input())

l = 0
r = n-1

c = 0

while l < r:
    while l < r and a[l] == 'R': l += 1
    while l < r and a[r] == 'W': r -= 1
    
    if a[l] == 'W' and a[r] == 'R':
        c += 1
        a[l] = 'R'
        a[r] = 'W'

print(c)