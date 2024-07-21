def dfs(n, cnt):
  global ans

  if ans >= (cnt + L - n):
    return
  
  if n == L:
    ans = max(ans, cnt)
    return
  
  for x, y in lst[n]:
    if visited[x - y] == 0:
      visited[x - y] = 1
      dfs(n + 1, cnt + 1)
      visited[x - y] = 0
  
  dfs(n + 1, cnt)

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 0

lst = [[] for _ in range(2 * N)]

for i in range(N):
  for j in range(N):
    if maps[i][j] == 1:
      lst[i + j].append((i, j))

L = 2 * N - 1
visited = [0] * (2 * N)

dfs(0, 0)

print(ans)