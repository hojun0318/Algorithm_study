def dfs(n, cnt):
  global ans
  
  if n == N:
    ans = max(ans, cnt)
    return
  
  if arr[n][0] <= 0:
    dfs(n + 1, cnt)

  else:
    flag = False
    for i in range(N):
      if n == i or arr[i][0] <= 0:
        continue

      flag = True
      
      arr[n][0] -= arr[i][1]
      arr[i][0] -= arr[n][1]
      dfs(n + 1, cnt + int(arr[n][0] <= 0) + int(arr[i][0] <= 0))
      arr[n][0] += arr[i][1]
      arr[i][0] += arr[n][1]
    
    if flag == False:
      dfs(n + 1, cnt)


N = int(input())
arr = []
ans = 0

for _ in range(N):
  # Stability,  Weight
  S, W = map(int, input().split())
  arr.append([S, W])


dfs(0, 0)

print(ans)