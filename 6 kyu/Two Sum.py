# Index method

def two_sum(num, target):
    for i, n in enumerate(num):
        x = target - n
        if x in num and num.index(x) != i:
            return [i, num.index(target-n)]

# Hashmap method

def two_sum(num, target):
    res = {}
    for i,v in enumerate(num):
        x = target - v
        if x in res:
            return [res[x],i]
        else:
            res[v] = i
            
 
