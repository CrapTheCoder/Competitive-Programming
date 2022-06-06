for _ in range(int(input())):
s = sorted(input())

l = [ord(i) for i in s]

if all(l[i] - l[i-1] == 1 for i in range(1, len(s))):
print('Yes')
else:
print('No')