def main():
    import os
    print(max(price * i for i, price in enumerate(sorted(map(int, os.read(0, 9000000).split()[1:]), reverse=True), 1)))
main()