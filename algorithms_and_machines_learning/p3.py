# 1 Check if Symmetric

def check_if_symmetric(string):
    for i,s in enumerate(string):
        if string[i] != string[-i-1]:
            return False
    return True

def check_if_symmetric_f(s: str) -> bool:
    return s == s[::-1]

# 2 Convert to numbers
def convert_to_numbers(string):
    letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    scores = list(range(28))
    numbers = []
    for letter in string:
        numbers.append(scores[letters.index(letter)])
    return numbers

# 3 convert to letters
def convert_to_letters(numbers):
    letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = list(range(28))
    result = ''
    for num in numbers:
        result += letters[nums.index(num)]
    return result

# 4 Return array that consists of elements in both array1 and array2
def get_intersection(array1, array2):
    output = []
    for element in array1:
        if element in array2 and element not in output:
            output.append(element)
    return output

# 5 return array consisting of elements in either array
def get_union(array1, array2):
    output = []
    for e in array1:
        if e not in output:
            output.append(e)
    for e in array2:
        if e not in output:
            output.append(e)
    return output

# 6 count number of each character in a string into a dictionary
# Output not sorted
def count_characters(string):
    output = {}
    string = str.lower(string)
    for c in string:
        if c not in output.keys():
            output[c] = 1
        else:
            output[c] += 1
    return output

# 7 Check if prime
def is_prime(N):
    max = int(N/2)
    counter = 0
    for n in range(2,max+1):
        if N % n == 0:
            counter += 1
    return counter == 0