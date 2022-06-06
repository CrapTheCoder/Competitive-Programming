for _ in range(int(input())):
    n = list(map(int, list(input())))
 
    if n[-1] % 2 == 0:
        print(0)
        continue
 
    if all(i % 2 for i in n):
        print(-1)
        continue
 
    if n[0] % 2 == 0:
        print(1)
        continue
 
    print(2)