def binary_ascii_to_decimal(string):
    if len(string) == 1:
        return int(string)
    number = (ord(string[0])-ord('0'))
    rest = binary_ascii_to_decimal(string[1:])
    return  number * (2**(len(string)-1)) + rest