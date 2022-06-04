for tc in range(int(input())):
    nums = '0123456789'
    str1 = input().strip()
    sum_str = 0
    for i in str1:
        if i in nums:
            sum_str = sum_str + int(i)

    if len(str1) == 0:
        print(0)
    else:
        print(sum_str)