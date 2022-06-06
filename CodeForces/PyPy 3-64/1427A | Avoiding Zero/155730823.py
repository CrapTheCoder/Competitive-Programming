range(int(input())):
int(input())
list(map(int, input().split()))

(a) == 0:
print('NO')


print('YES')

pt = sum(i for i in a if i > 0)
nt = -sum(i for i in a if i < 0)

print(*sorted(a, reverse=pt>nt))