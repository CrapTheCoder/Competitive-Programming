def main():
    import bisect
    
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
    
        disks = []
    
        for e in a:
            i = bisect.bisect(disks, e)
    
            if i == len(disks):
                disks.append(e)
            else:
                if disks[i] == e:
                    i += 1
        
                if i == len(a):
                    disks.append(e)
                else:
                    disks[i] = e
    
        print(len(disks), *disks)

main()