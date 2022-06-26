def high_and_low(n):
    n = n.split()
    n = [int(i) for i in n]
    return str(max(n))+" "+str(min(n))

high_and_low("8 3 -5 42 -1")
