from collections import deque

def bfs(tlst):
  # [0] 큐 생성 및 방문 배열 등 필요한 변수 생성
  queue = deque()
  visited = [[0] * (M + 2) for _ in range(N + 2)]
  cnt = 0

  # 큐에 초기데이터 삽입(방문 표시)
  for i in range(TC):
    if tlst[i] == 0:
      continue

    ti, tj = lst[i]
    queue.append((ti, tj))
    visited[ti][tj] = tlst[i]

  while queue:
    ci, cj = queue.popleft()
    if visited[ci][cj] == 25000:
      continue
    
    # 4방향, 범위내(X), (미방문), 호수나 꽃이 아니면
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
      ni = ci + di
      nj = cj + dj

      if seeds[ni][nj] == 0 or visited[ni][nj] == 25000:
        continue

      if visited[ni][nj] == 0:                    # 처음 방문
        if visited[ci][cj] < 0:                   # R : 1 감소
          visited[ni][nj] = visited[ci][cj] - 1
          queue.append((ni, nj))
        else:                                     # G : 1 증가
          visited[ni][nj] = visited[ci][cj] + 1
          queue.append((ni, nj))

      else:                                       # 이미 기록 -> 꽃 체크
        if visited[ci][cj] < 0:                   # R
          if visited[ni][nj] + visited[ci][cj] - 1 == 0:
            cnt += 1
            visited[ni][nj] = 25000

        else:
          if visited[ni][nj] + visited[ci][cj] + 1 == 0:
            cnt += 1
            visited[ni][nj] = 25000

  return cnt


def dfs(n, rcnt, gcnt, tlst):
  global ans
  if n == TC:                            # 모든 땅을 결정 했으면 종료
    if rcnt == RC and gcnt == GC:
      ans = max(ans, bfs(tlst))
    return
  
  dfs(n + 1, rcnt + 1,  gcnt,      tlst + [-1])      # 빨강 씨앗
  dfs(n + 1, rcnt,      gcnt + 1,  tlst + [1])       # 초록 씨앗
  dfs(n + 1, rcnt,      gcnt,      tlst + [0])       # 안 뿌리는 경우




N, M, RC, GC = map(int, input().split())
seeds = [[0] * (M + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]

lst = []
for i in range(1, N + 1):
  for j in range(1, M + 1):
    if seeds[i][j] == 2:                          # 배양액 가능한 땅이면(좌표 저장)
      lst.append((i, j))

TC = len(lst)

# [1] 가능한 모든 장소에 배양액 뿌리는 방법 순회
ans = 0
dfs(0, 0, 0, [])

print(ans)