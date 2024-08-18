N = int(input())
lst = [1000] + sorted(list(map(int, input().split())), reverse = True)

dp = [0] * (N + 1)

for i in range(1, N):
  mn = 1000
  for j in range(0, i):
    if lst[i] < lst[j]:
      mn = min(mn, lst[j])

  dp[i] = mn + 1

print(max(dp))