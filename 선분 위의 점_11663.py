def find_start(lst, t):
  s, e = 0, N - 1
  while s <= e:
    mid = (s + e) // 2
    if lst[mid] < t:
      s = mid + 1
    else:
      e = mid - 1
  return s


def find_end(lst, t):
  s, e = 0, N - 1
  while s <= e:
    mid = (s + e) // 2
    if lst[mid] <= t:
      s = mid + 1
    else:
      e = mid - 1
  return s


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lines = [list(map(int, input().split())) for _ in range(M)]

lst.sort()

for line in lines:
  s, e = line
  s_idx = find_start(lst, s)
  e_idx = find_end(lst, e)

  print(e_idx - s_idx)