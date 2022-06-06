for _ in range(int(input())):
    n = int(input())
 
    if n == 1:
        print(-1)
        continue
 
    s = '3' * (n - 1) + '4'
 
    print(s)