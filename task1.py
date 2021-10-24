def reverse_digits(n):
    if abs(n) >= 0xffffffff:
        return 0
    if n >= 0:
        n = str(n)
        return n[::-1]
    else:
        n = str(n)
        n = n[1:]
        n = '-' + n[::-1]
        return n


result = reverse_digits(-1243)
print(result)