for _ in range(int(input())):
    a, b = map(int, input().split())
 
    xor = 0
 
    for i in range(max(len(bin(a)), len(bin(b)))):
        if (a // 2 ** i) % 2 == (b // 2 ** i) % 2 == 1:
            xor += 2 ** i
 
    print((a ^ xor) + (b ^ xor))