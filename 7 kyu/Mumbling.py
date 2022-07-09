def accum(s):
    return '-'.join((char * i).title() for i, char in enumerate(s, 1))
