def get_sum(a,b):
    if a == b:
        return a
    lower, higher = sorted([a,b])
    return sum([i for i in range(lower,higher+1)])
