from itertools import combinations, product


class Text_combination:
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

    def generate_letters(self, number):
        if number == "":
            return []
        arrays = []
        result = []
        for char in number:
            arrays.append(self.numbers[char])
        arrays = product(*arrays)
        for array in arrays:
            result.append(''.join(list(array)))
        return result

task2 = Text_combination()
print(task2.generate_letters("46"))
