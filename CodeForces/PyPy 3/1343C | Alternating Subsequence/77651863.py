for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    max_till_now = a[0]
 
    s = 0
 
    for i in range(1, n):
        if (a[i] < 0) != (max_till_now < 0):
            s += max_till_now
            max_till_now = float('-inf')
 
        max_till_now = max(max_till_now, a[i])
 
    s += max_till_now
 
    print(s)