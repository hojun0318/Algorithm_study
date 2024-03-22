from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  visited_bfs = [[0] * 5 for _ in range(5)]
  visited_bfs[x][y] = 1
  cnt = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < 5 and 0 <= ny < 5 and visited_bfs[nx][ny] == 0 and visited_7[nx][ny] == 1:
        queue.append((nx, ny))
        visited_bfs[nx][ny] = 1
        cnt += 1

  return cnt == 7

def check():
  for i in range(5):
    for j in range(5):
      if visited_7[i][j] == 1:
        return bfs(i, j)


def dfs(n, cnt, scnt):
  global ans
  if cnt > 7:                           # 가지치기 : 이미 7명을 넘었으면 7공주 불가!
    return
  if n == 25:
    if cnt == 7 and scnt >= 4:          # 7명 그룹이고, 4명 이상이 이다솜 무리(S)의 학생인 경우
      if check():                       # 인접했는지 체크해서 모두 인접시 정답 + 1
        ans += 1
    return
  
  visited_7[n // 5][n % 5] = 1          # 포함하는 경우 표시
  dfs(n + 1, cnt + 1, scnt + int(arr[n // 5][n % 5] == 'S'))
  visited_7[n // 5][n % 5] = 0          # 원상 복구
  dfs(n + 1, cnt, scnt)                 # 포함하지 않는 경우




arr = [list(map(str, input())) for _ in range(5)]

ans = 0
visited_7 =  [[0] * 5 for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 학생번호(0 ~ 24) , 포함한 학생 수, 이다솜 무리(S) 학생 수
dfs(0, 0, 0)

print(ans)