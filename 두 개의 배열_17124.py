def search_min(lst):
  mn = lst[2]
  cursor = 2
  for i in range(2):
    if mn >= lst[i]:
      mn = lst[i]
      cursor = i
      
  return cursor


def binary_search(a, B, s, e):
  diff = e - s
  if diff <= 1:
      return s
  
  mid = (e + s) // 2
  
  if a < B[mid]:
      return binary_search(a, B, s, mid)
  else:
      return binary_search(a, B, mid, e)



T = int(input())

for _ in range(T):
  n, m = map(int, input().split())
  A = list(map(int, input().split()))
  B = sorted(list(map(int, input().split())))
  C = 0
  
  for a in A:
    idx = binary_search(a, B, 0, m)
    lst = [abs(a - B[idx - 1]), abs(a - B[idx]), abs(a - B[(idx + 1) % m])]
    C += B[idx + search_min(lst) - 1]
                

  print(C)