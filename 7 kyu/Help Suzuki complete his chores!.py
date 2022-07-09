def chore_assignment(chores):
    res = []
    while len(chores) > 0:
        res.append(max(chores) + min(chores))
        chores.remove(max(chores))
        chores.remove(min(chores))
        
    res.sort()
    return res
