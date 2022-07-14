def count_positives_sum_negatives(arr):
    positive = [i for i in arr if i >= 1]
    negative = [i for i in arr if i <= -1]
    return [] if arr == [] else [len(positive),sum(negative)]
