# N, M = map(int, input().split())
# resources = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0] * M for _ in range(N)]

# for i in range(N - 1):
#   for j in range(M - 1):
#     dp[i + 1][j + 1] = resources[i + 1][j + 1] + max((resources[i][j] + dp[i + 1][j]) , (resources[i][j] + dp[i][j + 1]))

# for k in dp:
#   print(k)

# print(dp[N - 1][M - 1])

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, M + 1):
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + maps[i - 1][j - 1]

print(dp[N][M])

for k in dp:
  print(k)