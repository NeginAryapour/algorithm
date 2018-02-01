def ascii_to_decimal(string):
    if len(string) == 0:
        return 0
    number = ord(string[0]) - 48  # 48 = ord('0')
    power = len(string) - 1
    return number * (10 ** power) + ascii_to_decimal(string[1:])


if __name__ == '__main__':
    if ascii_to_decimal('12345') == 12345:
        print(True)
    else:
        print(False)