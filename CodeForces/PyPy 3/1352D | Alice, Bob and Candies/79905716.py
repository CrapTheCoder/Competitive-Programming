for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    alice = a[0]
    bob = 0
 
    l = 1
    r = n-1
 
    moves = 1
    prev = a[0]
 
    while l <= r:
        cs = 0
 
        if moves % 2 == 0:
            while l <= r:
                cs += a[l]
                l += 1
 
                if cs > prev:
                    break
 
            alice += cs
 
        if moves % 2 == 1:
            while l <= r:
                cs += a[r]
                r -= 1
 
                if cs > prev:
                    break
 
            bob += cs
 
        prev = cs
        moves += 1
 
    print(moves, alice, bob)