def square_digits(num):
    res = ""
    for digit in str(num) :
        res += str(int(digit) ** 2)
        
    return int(res)
