def dig_pow(n,p):
  k = n
  digits = []
  while n > 0:
    digits.append(n%10)
    n //= 10
  digits = digits[::-1]
  number = sum([(digits[i]**(p+i) for i in range(len(digits))])
  return number/k if (number%k) == 0 else -1
