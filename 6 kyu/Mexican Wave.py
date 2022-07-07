def wave(str):    
    if len(str) == 0:
        return []
    else:
        str = str.lower()
        res = []
        for e,i in enumerate(str):
            if i == " ":
                continue
            else:
                res.append(str[:e] + str[e].upper() + str[e+1:])
        return res
