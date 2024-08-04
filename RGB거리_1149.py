N = int(input())
R = [0]
G = [0]
B = [0]
dp = [[0] * 3 for _ in range(N + 1)]

for _ in range(N):
  r, g, b = map(int, input().split())
  R.append(r)
  G.append(g)
  B.append(b)

dp[1][0] = R[1]
dp[1][1] = G[1]
dp[1][2] = B[1]

for i in range(2, N + 1):
  dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + R[i]
  dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + G[i]
  dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + B[i]

print(min(dp[N]))