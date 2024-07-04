def factorial_iterative(n):
  result = 1

  for i in range(1, n + 1):
    result *= i
  
  return result

print(factorial_iterative(10))


def factorial_recursive(m):
  if m <= 1:
    return 1
  
  return m * factorial_recursive(m - 1)

print(factorial_recursive(10))