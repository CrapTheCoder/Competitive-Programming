n1, n2, n3 = map(int, input().split())
s1 = set([int(input()) for _ in range(n1)])
s2 = set([int(input()) for _ in range(n2)])
s3 = set([int(input()) for _ in range(n3)])

ans = ((s1 & s2) | (s2 & s3) | (s1 & s3))

print(len(ans))
print(*sorted(ans), sep='\n')