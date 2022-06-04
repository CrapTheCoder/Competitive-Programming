s = input()
print(sum(map(ord, s[:len(s) // 2 + len(s) % 2])))