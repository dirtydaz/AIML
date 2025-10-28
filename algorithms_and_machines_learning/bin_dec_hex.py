# Converting between binary decimal and hexidecimal

# 1 Binary to Decimal
def binary_to_decimal(string):
    counter = 0
    for i in range(len(string)):
        counter += int(string[-i-1])*2**(i)
    print(counter)

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
    print(counter)

# 3 Decimal to Binary
def decimal_to_binary(string):


