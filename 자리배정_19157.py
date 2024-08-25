C, R = map(int, input().split())
K = int(input())

seat_lst = [[0] * C for _ in range(R)]
seat_num = [[[] * 2 for _ in range(C)] for _ in range(R)]

max_num_seat = C * R
flag = False

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작값 초기화
x = R - 1
y = dr = 0
i = 1
j = 0

for cnt in range(1, max_num_seat + 1):
  seat_lst[x][y] = cnt
  # 다음 위치
  nx = x + dx[dr]
  ny = y + dy[dr]
  # 좌석 번호 갱신
  if dr == 0:
    i, j = i, j + 1
  elif dr == 1:
    i, j = i + 1, j
  elif dr == 2:
    i, j = i, j - 1
  else:
    i, j = i - 1, j

  seat_num[x][y].append([i, j])

  # 다음 위치가 범위 내에 있고, 빈 값(0)이라면
  if 0 <= nx < R and 0 <= ny < C and seat_lst[nx][ny] == 0:
    x, y = nx, ny
  # 이동 리스트 인덱스 및 다음 위치 갱신
  else:
    dr = (dr + 1) % 4
    x = x + dx[dr]
    y = y + dy[dr]

# 대기번호 좌석 찾기
for r in range(R):
  for c in range(C):
    if seat_lst[r][c] == K:
      a = seat_num[r][c][0][0]
      b = seat_num[r][c][0][1]
      flag = True

# 대기번호 좌석이 있으면 좌석 출력, 없으면 0 출력
if flag:
  print(a, b)
else:
  print(0)