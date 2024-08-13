def search_min(lst):
  mn = lst[2]
  cursor = 2
  if lst[1] <= mn:
      mn = lst[1]
      cursor = 1
  if lst[0] <= mn:
      cursor = 0
      
  return cursor


def binary_search(a, B, s, e):
  diff = e - s
  if diff <= 1:
      return s
  
  m = (e + s) // 2
  
  if a < B[m]:
      return binary_search(a, B, s, m)
  else:
      return binary_search(a, B, m, e)



T = int(input())

for _ in range(T):
  n, m = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  B.sort()
  C = 0
  
  for a in A:
    idx = binary_search(a, B, 0, m)
    lst = []
    lst.append(abs(a - B[idx - 1]))
    lst.append(abs(a - B[idx]))
    lst.append(abs(a - B[(idx + 1) % m]))
    chk = search_min(lst)
    C += B[idx + chk - 1]
                

  print(C)