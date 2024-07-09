def dfs(n):
  global ans
  if n == N:
    ans += 1
    return
  
  for i in range(N):
    if visited1[i] == visited2[n + i] == visited3[n - i] == 0:
      visited1[i] = visited2[n + i] = visited3[n - i] = 1
      dfs(n + 1)
      visited1[i] = visited2[n + i] = visited3[n - i] = 0




N = int(input())

ans = 0
visited1 = [0] * N
visited2 = [0] * (N * 2)
visited3 = [0] * (N * 2)

dfs(0)

print(ans)