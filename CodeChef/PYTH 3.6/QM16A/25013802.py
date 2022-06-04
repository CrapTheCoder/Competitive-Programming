for _ in range(int(input())):
    s1 = set(input().split())
    s2 = set(input().split())
    
    if s1.intersection(s2):
        print('Yes')
    else:
        print('No')
