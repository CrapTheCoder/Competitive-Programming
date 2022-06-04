for _ in range(int(input())):
    s = input().lower()

    if 'berhampore' in s and 'serampore' in s: print('Both')
    elif 'berhampore' in s: print('GCETTB')
    elif 'serampore' in s: print('GCETTS')
    else: print('Others')