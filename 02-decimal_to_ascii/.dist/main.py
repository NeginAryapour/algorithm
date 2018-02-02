def decimal_to_ascii(number):
    if number == 0 :
        return ''
    int_number = chr((number % 10) + ord('0'))
    return decimal_to_ascii(number // 10) + int_number