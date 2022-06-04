s = input().strip().upper()
print(sum(ord(i) - ord('A') + 1 + ord('Z') - ord(i) + 1 for i in s) - sum(ord(i) - ord('A') for i in s))