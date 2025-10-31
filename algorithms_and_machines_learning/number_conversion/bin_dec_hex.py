# Converting between binary decimal and hexidecimal

# 1 Binary to Decimal
def binary_to_decimal(string):
    counter = 0
    for i in range(len(string)):
        counter += int(string[-i-1])*2**(i)
    return counter

# 2 Hex to Decimal
def hexadecimal_to_decimal(string):
    counter = 0 
    size = len(string)
    vals = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    # Need to check for value being a number or a letter
    for i in range(size):
        if string[i].isdigit():
            counter += int(string[i])*16**(size-i-1)
        elif string[i].isalpha():
            counter += vals[string[i]]*16**(size-i-1)
        else: 
            print('Not hexadecimal')
            return 
    return counter

# 3 Decimal to Binary
def decimal_to_binary(string):
    if string == '0':
        return print('0')
    
    binary = ''
    counter = int(string)
    ones = []
    while counter > 0:
        i = 0
        while 2**i <= counter:
            i += 1
        counter -= 2**(i-1)
        ones.append(i-1)

    for i in range(max(ones),-1,-1):
        if i in ones:
            binary += '1'
        else:
            binary += '0'
    return binary

# 4 Decimal to Hexadecimal
def decimal_to_hexadecimal(string):
    if string == '0':
        return print('0')
    vals = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex = ''
    counter = int(string)
    places = {}

    while counter > 0:
        i = 0
        n = 1
        while 16**i <= counter:
            i += 1
        while n*16**(i-1) <= counter:
            n +=1
        counter -= (n-1)*16**(i-1)
        places[i-1] = n-1

    for i in range(max(places),-1,-1):
        if i in places.keys() and places[i] < 10:
            hex += str(places[i])
        elif i in places.keys() and places[i] >= 10:
            hex += str(vals[places[i]])
        else:
            hex += '0'
    
    return hex

# 5 Binary to Hexadecimal
def binary_to_hexadecimal(string):
    decimal = binary_to_decimal(string)
    hexadecimal = decimal_to_hexadecimal(decimal)
    return hexadecimal

# 6 Hexadecimal to Binary
def hexadecimal_to_binary(string):
    decimal = hexadecimal_to_decimal(string)
    binary = decimal_to_binary(decimal)
    return binary