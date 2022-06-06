for _ in range(int(input())):
    s = input()
    x = sorted(len(i) for i in s.split('0') if len(i) > 0)
 
    print(max(sum(x[::2]), sum(x[1::2])))