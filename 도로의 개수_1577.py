def Block():
  for _ in range(K):
    a, b, c, d = map(int, input().split())
    if a > c:
      a, c = c, a
    if b > d:
      b, d = d, b
    if c - a > d - b:
      dp[a][b][1] = -1
    else:
      dp[a][b][2] = -1

def Find():
  for x in range(N + 1):
    for y in range(M + 1):
      for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= N and 0 <= ny <= M:
          if dp[x][y][i + 1] != -1:
            dp[nx][ny][0] += dp[x][y][0]

  return dp[N][M][0]

# 입력 받기
N, M = map(int, input().split())
K = int(input())
# DP 테이블 생성 및 초기화
dp = [[[0] * 3] + [[0] * 3 for _ in range(M)] for _ in range(N + 1)]
dp[0][0][0] = 1
# 방향(하, 우)
dx = [1, 0]
dy = [0, 1]

# 공사로 못가는 곳
Block()
# 최단 거리 DP수행
ans = Find()

print(ans)