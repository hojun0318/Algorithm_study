A, B, C = map(int, input().split())

def POW(a, b, c):
  if b == 1:
    return a % c
  elif b % 2 == 0:
    return (POW(a, b // 2, c) ** 2) % C
  else:
    return ((POW(a, b // 2, c) ** 2) * a) % C
  
print(POW(A, B, C))