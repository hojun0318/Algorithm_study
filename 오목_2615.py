def check(si, sj, di, dj, c):
  if maps[si - di][sj - dj] == c:
    return False

  return True
  

def solve(si, sj, c):
  for di, dj in ((0, 1), (1, 0), (1, 1), (-1, 1)):
    cnt = 0
    for mul in range(6):
      ni = si + di * mul
      nj = sj + dj * mul

      if 0 <= ni < N and 0 <= nj < N and maps[ni][nj] == c:
        cnt += 1
      else:
        break
    if cnt == 5 and check(si, sj, di, dj, c):
      return 'TRUE'
  
  return 'FALSE'


N = 19
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 'NO'

for c in range(1, 3):
  for i in range(N):
    for j in range(N):
      if maps[i][j] == c:
        if solve(i, j, c) == 'TRUE':
          ans = 'YES'
          print(c)
          print(i + 1, j + 1)
          exit(0)

if ans == 'NO':
  print(0)