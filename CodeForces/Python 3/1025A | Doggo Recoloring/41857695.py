n = int(input())
s = input()
 
print('Yes' if n < 2 or any(s.count(i) > 1 for i in set(s)) else 'No')