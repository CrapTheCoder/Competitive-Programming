s = input()
t = int(input())
while t > 0:
    a, b = map(int, input().split())
    if s[(a - 1) % len(s)] == s[(b - 1) % len(s)]:
        print("Yes")
    else:
        print("No") 
    t -= 1 