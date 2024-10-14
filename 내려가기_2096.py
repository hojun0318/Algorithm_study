N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
flag = True
ans = []

for _ in range(2):
  dp = [[0] * 3 for _ in range(N)]
  dp[0] = maps[0]

  if flag == True:
    for i in range(1, N):
      dp[i][0] = maps[i][0] + max(dp[i - 1][0], dp[i - 1][1])
      dp[i][1] = maps[i][1] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
      dp[i][2] = maps[i][2] + max(dp[i - 1][1], dp[i - 1][2])

    ans.append(max(dp[N - 1]))

  if flag == False:
    for i in range(1, N):
      dp[i][0] = maps[i][0] + min(dp[i - 1][0], dp[i - 1][1])
      dp[i][1] = maps[i][1] + min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
      dp[i][2] = maps[i][2] + min(dp[i - 1][1], dp[i - 1][2])
  
    ans.append(min(dp[N - 1]))

  flag = False

print(*ans)