from string import ascii_lowercase as alpha

# cook your dish here
for tc in range(int(input())):
    str1 = input().strip()
    sum_str = 0
    for i in str1:
        if i not in alpha:
            sum_str = sum_str + int(i)

    if len(str1) == 0:
        print(0)
    else:
        print(sum_str)