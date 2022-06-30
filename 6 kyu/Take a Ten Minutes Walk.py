def is_valid_walk(walk):
    if len(walk) == 10:
        if walk.count("n") == walk.count("s") and walk.count("w") == walk.count("e"):
            return print(True)
        else:
            return print(False)
    else:
        return print(False)