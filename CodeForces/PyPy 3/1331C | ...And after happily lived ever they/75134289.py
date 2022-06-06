x = bin(int(input()))[2:].zfill(6)

print(int(x[0] + x[5] + x[3] + x[2] + x[4] + x[1], 2))