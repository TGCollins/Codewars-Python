def series_sum(n):
    series = [1/(1+i*3) for i in range(n)]
    return "{:.2f}".format(sum(series))
