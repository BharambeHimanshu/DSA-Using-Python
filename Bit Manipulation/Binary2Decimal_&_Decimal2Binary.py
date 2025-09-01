# Decimal to Binary     TC - o(log2n)     SC -> o(log2n)
num = 13

def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result += "1" if (n % 2) else "0"  # append current bit
        n //= 2
    return result[::-1]  # reverse to correct order

print(decimal_to_binary(num))


# Convert Binary to Decimal      TC -> o(N)       SC ->o(1)

str = "1101"

def binary2decimal(str):
    decimal_number = 0
    power = 0
    index = len(str) - 1
    while index >= 0:
        num = int(str[index]) * (2**power)
        decimal_number += num
        index -= 1
        power += 1
    return decimal_number

print(binary2decimal(str))