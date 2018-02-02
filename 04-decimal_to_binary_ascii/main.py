def decimal_to_asci(number):
    if number == 0 :
        return []
    return decimal_to_asci(number//2) + [number%2]

def list_to_int(list):
    string = ''
    for member in list :
        string = string +''.join(str(member))
    return string