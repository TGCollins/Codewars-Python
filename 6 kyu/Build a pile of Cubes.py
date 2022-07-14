def find_nb(m):
    res = 0
    n = 1
    while res <= m:
        res += n**3
        if(res==m): return n
        n += 1
    return -1
