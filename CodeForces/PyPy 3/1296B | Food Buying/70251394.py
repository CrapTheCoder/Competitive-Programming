for _ in range(int(input())):
    x = 0
 
    n = int(input())
 
    while n >= 10:
        j = len(str(n)) - 1
 
        n -= 10 ** j
        n += 10 ** (j - 1)
 
        x += 10 ** j
 
    print(x + n)