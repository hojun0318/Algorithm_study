T = int(input())
dp = [0] * 12
dp[1:4] = [1, 2, 4]

for _ in range(T):
  N = int(input())

  for i in range(4, 12):
    dp[i] = sum(dp[i - 3: i])

  print(dp[N])