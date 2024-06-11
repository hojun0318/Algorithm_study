def dfs(n, lst):
  if n == 6:
    ans.append(lst)
    return
  
  for i in range(k):
    if lst:
      if not visited[i] and lst[-1] < S[i]:
        visited[i] = 1
        dfs(n + 1, lst + [S[i]])
        visited[i] = 0
    else:
      if not visited[i]:
        visited[i] = 1
        dfs(n + 1, lst + [S[i]])
        visited[i] = 0


while True:
  lst = list(map(int, input().split()))
  k = lst[0]
  S = lst[1:]

  if k == 0:
    break
  
  ans = []
  visited = [0] * k
  dfs(0, [])

  for lst in ans:
    print(*lst)
  print()