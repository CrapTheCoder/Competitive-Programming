for _ in range(int(input())):
    n = int(input())
    s = input()
    print(max(sum(s[i] == s[i+1] == '1' for i in range(n-1)),
              sum(s[i] == s[i+1] == '0' for i in range(n-1))))