vowels = 'aeiou'

def find_max(n, s):
    maxi = 0
    current = 0

    for i in range(n):
        if s[i] in vowels:
            current += 1

            if i + 1 == n:
                break

            if s[i] == s[i+1]:
                maxi = max(maxi, current)
                current = 0
        else:
            maxi = max(maxi, current)
            current = 0

    return max(maxi, current)

for _ in range(int(input())):
    n = int(input())
    s = input()

    print(find_max(n, s))
