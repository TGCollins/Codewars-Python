def count_sheep(n):
    if n == 0:
        return ''    
    return ''.join(f'{i} sheep...' for i in range(1,n+1))
