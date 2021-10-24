class Reverse_numbers:
    def __init__(self):
        self.n = 0

    def reverse_digits(self, n):
        self.n = n
        if abs(self.n) >= 0xffffffff:
            return 0
        if self.n >= 0:
            self.n = str(n)
            return n[::-1]
        else:
            self.n = str(self.n)
            self.n = self.n[1:]
            self.n = '-' + self.n[::-1]
            return int(self.n)


result = Reverse_numbers()
result.reverse_digits(-1243)
print(result.n)
