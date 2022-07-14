# If else method

def arithmetic(a, b, operator):
    if operator == "add":
        return a+b
    elif operator == "subtract":
        return a-b
    elif operator == "multiply":
        return a*b
    else:
        return a/b
      
 # Dictionary Method

def arithmetic(a, b, op):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[op]
