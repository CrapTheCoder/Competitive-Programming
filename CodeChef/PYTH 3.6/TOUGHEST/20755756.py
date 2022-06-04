n = int(input())
a = input().split()

print(sum(not sum(list(map(int, i))) % 3 for i in a))