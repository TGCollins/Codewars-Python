# Method 1

def first_non_consecutive(arr):
    for i, j in enumerate(arr, arr[0]):
        if j != i:
            return j

# Method 2

def first_non_consecutive(arr):
  i=1
  for x in arr:
    if i<len(arr) and arr[i]-arr[i-1] != 1:
      return arr[i]
    i+=1
      return none
    
