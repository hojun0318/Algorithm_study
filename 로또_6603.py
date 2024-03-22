def dfs(n, lst):
  if n == 6:
    ans.append(lst)
    return
  
  for i in range(1, len(arr)):
    if not lst:
      if visited[i] == 0:
        visited[i] = 1
        dfs(n + 1, lst + [arr[i]])
        visited[i] = 0
    else:
      if visited[i] == 0:
        if lst[-1] < arr[i]:
          visited[i] = 1
          dfs(n + 1, lst + [arr[i]])
          visited[i] = 0

while True:
  arr = list(map(int, input().split()))
  k = arr[0]
  if k == 0:
    break

  visited = [0] * len(arr)
  ans = []

  dfs(0, [])

  for lst in ans:
    print(*lst)
  print()