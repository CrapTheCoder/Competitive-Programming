for _ in range(int(input())):
    n = int(input())

    bit = 1
    nibble = 0
    byte = 0

    while True:
        if bit:
            n -= 2

            if n < 1:
                break

            nibble = bit
            bit = 0

        if nibble:
            n -= 8

            if n < 1:
                break

            byte = nibble
            nibble = 0

        if byte:
            n -= 16

            if n < 1:
                break

            bit = byte * 2
            byte = 0

    print(bit, nibble, byte)
