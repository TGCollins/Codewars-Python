from collections import Counter

def xo(s):
    c = Counter(s.lower())
    if c["x"] == c["o"]:
        return True
    else:
        return False