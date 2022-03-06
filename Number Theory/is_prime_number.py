
import math

def is_prime_number(x):
  if x==0 or x==1:
    return False
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      return False #소수가 아니면 False반환
  return True #소수면 True반환
