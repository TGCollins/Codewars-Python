def solution(string, ending):
    back = len(ending)*(-1)
    end = string[back:]
    if end == ending or ending == '':
        return True
    else:
        return False