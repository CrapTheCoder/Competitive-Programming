ans = int

a = int(input())
b = int(input())
s = input()

if s == '+':
    ans = a + b

if s == '-':
    ans = a - b

if s == '*':
    ans = a * b

if s == '/':
    ans = a / b

print(ans)