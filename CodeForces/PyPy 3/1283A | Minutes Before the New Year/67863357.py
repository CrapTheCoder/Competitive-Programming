for _ in range(int(input())):
    h, m = map(int, input().split())
 
    print(1440 - (h * 60 + m))