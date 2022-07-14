def sequence_sum(begin_number, end_number, step):
    list = [i for i in range(begin_number, end_number+1, step)]
    return sum(list)
