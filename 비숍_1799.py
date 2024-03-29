def dfs(n, cnt):
  global ans

  if ans >= (cnt + (L + 1 - n) // 2):
    return
  
  if n >= L:
    ans = max(ans, cnt)
    return
  
  for i, j in lst[n]:
    if visited[i - j] == 0:
      visited[i - j] = 1
      dfs(n + 2, cnt + 1)
      visited[i - j] = 0
  dfs(n + 2, cnt)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = [[] for _ in range(2 * N)]

for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      lst[i + j].append((i, j))

L = (2 * N) - 1
visited = [0] * (2 * N)

ans = 0
dfs(0, 0)
t = ans
dfs(1, 0)

print(ans + t)