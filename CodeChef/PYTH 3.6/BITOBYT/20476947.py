for _ in range(int(input())):
    n = int(input())

    bit = 1
    nibble = 0
    byte = 0

    while True:
        if bit:
            n -= 2

            if n <= 0:
                break

            nibble = bit
            bit = 0

        elif nibble:
            n -= 8

            if n <= 0:
                break

            byte = nibble
            nibble = 0

        elif byte:
            n -= 16

            if n <= 0:
                break

            bit = byte * 2
            byte = 0
    print(bit, nibble, byte)