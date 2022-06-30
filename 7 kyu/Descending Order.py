def descending_order(num):
    num = sorted([x for x in str(num)],reverse=True)
    num = int(''.join(num))
    return num