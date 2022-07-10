def calc(x):
    total1 = ''.join(str(ord(char)) for char in x)
    total2 = total1.replace("7","1")
    t1 = [int(i) for i in str(total1)]
    t2 = [int(i) for i in str(total2)]
    return sum(t1)-sum(t2)
