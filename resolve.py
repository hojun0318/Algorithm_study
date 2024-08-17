# 입력 받기
N = int(input())
stair = [0] + [int(input()) for _ in range(N)]

# dp 테이블 생성 및 초기화
dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
  # 안밟는 경우
  dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
  # 1번 밟는 경우
  dp[i][1] = dp[i - 1][0] + stair[i]
  # 2번 연속으로 밟는 경우
  dp[i][2] = dp[i - 1][1] + stair[i]

# 마지막 계단은 무조건 밟아야 함
print(max(dp[N][1:3]))