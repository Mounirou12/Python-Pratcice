def to_binary(n):
    return int (bin(abs(n))[2:])

def to_bin(n):
    return int (f'{n:b}')

print(to_binary(5))
print(to_bin(5))

