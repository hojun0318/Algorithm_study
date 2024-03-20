def dfs(n):
  global ans
  if n == N:
    ans += 1
    return
  
  for i in range(N):
    if visited1[i] or visited2[n + i] or visited3[n - i + N - 1]:
      continue
    else:
      visited1[i] = 1
      visited2[n + i] = 1
      visited3[n - i + N - 1] = 1
      dfs(n + 1)
      visited1[i] = 0
      visited2[n + i] = 0
      visited3[n - i + N - 1] = 0

N = int(input())
ans = 0

visited1 = [0] * N
visited2 = [0] * (N * 2 - 1)
visited3 = [0] * (N * 2 - 1)

dfs(0)

print(ans)