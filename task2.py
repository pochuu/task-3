from itertools import combinations, product

numbers = {
    '1': '',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def generate_letters(number):
    if number == "":
        return []
    arrays = []
    result = []
    for char in number:
        arrays.append(numbers[char])
    arrays = product(*arrays)
    for array in arrays:
        result.append(''.join(list(array)))
    return result

print(generate_letters("46"))
