def main():
    import os 
    
    arr = sorted(map(int, os.read(0, 9999999).split()[1:]), reverse=True)
    print(max(price * i for i, price in enumerate(arr, 1)))

main()