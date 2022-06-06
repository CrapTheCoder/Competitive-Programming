def op1(i):
global s
print('L', i)
s = s[1:i][::-1] + s

def op2(i):
global s
print('R', i)
s = s + s[i-1:len(s)-1][::-1]

s = input()

print(3)
op1(2)
# print(s)
op2(2)
# print(s)
op2(len(s) - 1)