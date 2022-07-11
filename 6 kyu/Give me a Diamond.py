def diamond(n):
    if n%2 == 0 or n<0:
        return None
    rows = []
    spaces = 1
    for i in range(1,n+1):
        if i%2 == 1:
            spaces = int(n-i//2)-int((n+1)/2)
            rows.append(" "*spaces + '*'*i)
    back = sorted(rows, reverse=True)
    total_rows = rows + back[1:]
    return (''.join(x +'\n' for x in total_rows))
