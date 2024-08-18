# 입력 받기
N = int(input())
lst = [1000] + list(map(int, input().split()))
# dp 테이블 생성 및 초기화
dp = [0] * (N + 1)

for i in range(1, N + 1):
  mx = 0
  # 0 ~ i - 1 중 max값 (현재보다 큰 값 중에서)
  for j in range(0, i):
    if lst[i] < lst[j]:
      mx = max(mx, dp[j])
  dp[i] = mx + 1


print(max(dp))