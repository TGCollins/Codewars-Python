def printer_error(s):
    errors = 0
    good = "abcdefghijklm"
    for char in s:
        if char not in good:
            errors += 1
    return  str(errors) + "/" + str(len(s))
