n, m = map(int, input().split())
 
s = input().split()
t = input().split()
 
for i in range(int(input())):
    x = int(input())
 
    print(s[x % n - 1] + t[x % m - 1])