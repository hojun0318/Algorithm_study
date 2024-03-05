from collections import defaultdict

# BFS

T = int(input())

for _ in range(T):
  n = int(input())
  p = [0] + list(map(int, input().split()))
  candidates = set(range(1, n + 1))
  res = n

  while candidates:
    c = candidates.pop()
    cnt = 1
    d = defaultdict(int)
    while True:
      d[c] = cnt
      cnt += 1
      if p[c] in candidates:
        candidates.remove(p[c])
        c = p[c]
      else:
        if d[p[c]] != 0:
          res -= cnt - d[p[c]]
        break

  print(res)