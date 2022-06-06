n = int(input())
a = list(map(int, input().split()))
 
mini = float('inf')
 
odd  = sorted(i for i in a if i % 2 == 1)
even = sorted(i for i in a if i % 2 == 0)
 
while odd and even:
    odd.pop()
    even.pop()
 
if odd:
    odd.pop()
 
mini = min(mini, sum(odd) + sum(even))
 
odd  = sorted(i for i in a if i % 2 == 1)
even = sorted(i for i in a if i % 2 == 0)
 
while even and odd:
    even.pop()
    odd.pop()
 
if even:
    even.pop()
 
mini = min(mini, sum(odd) + sum(even))
 
print(mini)