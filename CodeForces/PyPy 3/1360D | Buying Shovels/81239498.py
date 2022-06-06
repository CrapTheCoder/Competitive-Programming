def factors(n):
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            yield n // i
 
for _ in range(int(input())):
    n, k = map(int, input().split())
 
    mini = n
 
    for i in factors(n):
        if i <= k and n // i < mini:
            mini = n // i
 
    print(mini)