import math

def is_square(n):
    if n < 0:
        return False
    square_root = math.sqrt(n)
    number = int(square_root)
    return (number ** 2 == n)