def textToBin(message):
    temp = ""
    for ch in message:
        temp += numToHex(ord(ch))
    return hexToBin(temp)


def numToHex(num):
    num = int(num)
    if num < 0:
        print("Something went wrong")
        exit(0)
    if num == 0:
        return "00"
    temp = ""
    while num > 0:
        div = int(num/16)
        rem = num % 16
        num = div
        if rem >= 10:
            rem += 55
            temp += chr(rem)
        else:
            temp += str(rem)
    temp = temp[::-1]
    temp = "0" + temp if len(temp) == 1 else temp
    return temp


def hexToBin(hex):
    temp = ""
    for ch in hex:
        temp += hexMap[ch]
    return temp


hexMap = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
binMap = dict()

for key, value in hexMap.items():
    binMap[value] = key


def make64(bin):
    while not len(bin) % 64 == 0:
        bin += "0"
    parts = int(len(bin)/64)
    temp = []
    pos = 0
    for _ in range(parts):
        temp.append(bin[pos:pos+64])
        pos += 64
    return temp


def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans = ans + "0"
        else:
            ans = ans + "1"
    return ans


i_permutation = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24,
                 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
expansion = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
permutation = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18,
               31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
ip_inverse = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21,
              61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
permuted_choice1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52,
                    44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
permuted_choice2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20,
                    13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
s_boxes = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
           [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
           [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
           [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
           [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
           [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
           [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
           [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]


def permutedChoice1(key):
    temp = ""
    for pos in permuted_choice1:
        temp += key[pos-1]
    return temp


def permutedChoice2(key):
    temp = ""
    for pos in permuted_choice2:
        temp += key[pos-1]
    return temp


def circularShift(key, round):
    by = shift[round]
    return key[by:] + key[:by]


def keygen(key):
    subkeys = []
    key = permutedChoice1(key)
    for round in range(16):
        c0 = key[:28]
        d0 = key[28:]
        key = circularShift(c0, round) + circularShift(d0, round)
        subkeys.append(permutedChoice2(key))
    return subkeys


def iPermutation(message):
    temp = ""
    for pos in i_permutation:
        temp += message[pos-1]
    return temp


def expand(message):
    temp = ""
    for pos in expansion:
        temp += message[pos-1]
    return temp


def xor(message, key):
    if not len(message) == len(key):
        print("Something went wrong")
        exit(0)
    temp = ""
    for i in range(len(key)):
        if key[i] == message[i]:
            temp += "0"
        else:
            temp += "1"
    return temp


def binToDecimal(num):
    num = str(num)
    num = num[::-1]
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * (2**i)
    return decimal


def sBox(inp):
    parts = []
    pos = 0
    for _ in range(8):
        parts.append(inp[pos:pos+6])
        pos += 6

    result = ""
    c = 0
    for part in parts:
        row = part[0] + part[-1]
        column = part[1:len(part)-1]
        row = binToDecimal(row)
        column = binToDecimal(column)
        s_box = s_boxes[c]
        c += 1
        temp = s_box[row][column]
        temp = bin(temp).replace("0b", "")
        while not len(temp) == 4:
            temp = "0" + temp
        result += temp
    return result


def permute(message):
    temp = ""
    for pos in permutation:
        temp += message[pos-1]
    return temp


def rounds(message, subkeys):
    for round in range(16):
        l0 = message[:32]
        r0 = message[32:]
        temp = expand(r0)
        subkey = subkeys[round]
        temp = xor(temp, subkey)
        temp = sBox(temp)
        temp = permute(temp)
        r1 = xor(l0, temp)
        l1 = r0
        message = l1 + r1
    return message


def swap32(message):
    return message[32:] + message[:32]


def inversePermutation(message):
    temp = ""
    for pos in ip_inverse:
        temp += message[pos-1]
    return temp


def encryption(binMessage, key):
    subkeys = keygen(key)
    encoded = iPermutation(binMessage)
    encoded = rounds(encoded, subkeys)
    encoded = swap32(encoded)
    encoded = inversePermutation(encoded)
    return encoded


def decryption(binMessage, key):
    subkeys = keygen(key)
    subkeys = subkeys[::-1]
    encoded = iPermutation(binMessage)
    encoded = rounds(encoded, subkeys)
    encoded = swap32(encoded)
    encoded = inversePermutation(encoded)
    return encoded


def binToHex(message):
    parts = int(len(message)/4)
    temp = []
    pos = 0
    for _ in range(parts):
        temp.append(message[pos:pos+4])
        pos += 4
    hexadecimal = ""
    for bin in temp:
        hexadecimal += binMap[bin]
    return hexadecimal


def main():
    message = input("\nEnter your message\n")
    key = input("\nEnter you key\nKey length must be 8 characters\n")
    if not len(key) == 8:
        print("invalid key")
        exit(0)
    choice = input("\nChoose any option\n1. Encrypt\n2. Decrypt\n")
    key = textToBin(key)
    message = textToBin(message)
    parts = make64(message)
    if choice == "1":
        encoded = ""
        for part in parts:
            encoded += encryption(part, key)
        print(f"\nYour message - {binToHex(message)}")
        print(f"\nEncrypted message - {binToHex(encoded)}")
    elif choice == "2":
        decoded = ""
        for part in parts:
            decoded += decryption(part, key)
        print(f"\nYour cipher text - {binToHex(message)}")
        print(f"\nDecrypted message - {binToHex(decoded)}")
    else:
        print("Invalid Choice")
        exit(0)


if __name__ == "__main__":
    main()
