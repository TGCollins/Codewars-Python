def sort_array(arr):
    odd = sorted([i for i in arr if (i % 2) != 0])
    new = [i if (i % 2) == 0 else odd.pop() for i in arr]
    return print(new)
