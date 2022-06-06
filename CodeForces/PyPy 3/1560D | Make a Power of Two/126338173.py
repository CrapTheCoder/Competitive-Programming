l = []
for i in range(100):
    l.append(str(2 ** i))
 
for _ in range(int(input())):
    n = input()
    mini = float('inf')
 
    for k in l:
        i = 0
        c = 0
 
        for j in n:
            if i >= len(k):
                break
 
            if k[i] == j:
                i += 1
                c += 1
 
        mini = min(mini, (len(n) - c) + (len(k) - c))
 
    print(mini)