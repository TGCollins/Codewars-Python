def persistence(n):
    if len(str(n)) == 1:
        return 0
    t = 1
    for i in str(n):
        t *= int(i)
    return 1+persistence(t)
