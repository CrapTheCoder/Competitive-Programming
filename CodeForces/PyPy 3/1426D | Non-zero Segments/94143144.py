n = int(input())
a = list(map(int, input().split()))
 
d = {0}
cur_sum = 0
 
total = 0
 
for i in range(n):
    cur_sum += a[i]
 
    if cur_sum in d:
        total += 1
        cur_sum = a[i]
        d = {0}
 
    d.add(cur_sum)
 
print(total)