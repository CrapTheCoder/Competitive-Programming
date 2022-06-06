def divisors(n):
    l = []
 
    if not n % 2:
        l.append(2)
 
        while not n % 2:
            n //= 2
 
    i = 3
 
    while i * i <= n:
        if not n % i:
            l.append(i)
 
        while not n % i:
            n //= i
 
        i += 2
 
    if n > 2:
        l.append(n)
 
    return l
 
n = int(input())
x = divisors(n)
 
if len(x) == 1:
    print(x[0])
else:
    print(1)