H, W = map(int, input().split())
N = int(input())
stickers = []
ans = 0

for _ in range(N):
  R, C = map(int, input().split())
  area = R * C
  # 넓이, 로우, 컬럼
  stickers.append([area, R, C])

for i in range(N - 1):
  cnt = flag = 0
  size1, x1, y1 = stickers[i]

  # 가지치기
  if max(x1, y1) > max(H,W):
    continue

  flag += 1
  cnt += size1

  for j in range(i + 1, N):
    size2, x2, y2 = stickers[j]
    # 첫번째 스티커 회전 X
    if x1 <= H and y1 <= W:
      # 두번째 스티커 회전 X
      if x2 <= (H - x1) and y2 <= W:
        cnt += size2
        flag += 1
      elif x2 <= H and y2 <= (W - y1):
        cnt += size2
        flag += 1
      # 두번째 스티커 회전 O
      elif y2 <= (H - x1) and x2 <= W:
        cnt += size2
        flag += 1
      elif y2 <= H and x2 <= (W - y1):
        cnt += size2
        flag += 1
    # 스티커 2개 여부 확인
    if flag == 2:
      if cnt > ans:
        ans = cnt
      flag -= 1
      cnt -= size2
    # 첫번째 스티커 회전 O
    if y1 <= H and x1 <= W:
      # 두번째 스티커 회전 X
      if x2 <= (H - y1) and y2 <= W:
        cnt += size2
        flag += 1
      elif x2 <= H and y2 <= (W - x1):
        cnt += size2
        flag += 1
      # 두번째 스티커 회전 O
      elif y2 <= (H - y1) and x2 <= W:
        cnt += size2
        flag += 1
      elif y2 <= H and x2 <= (W - x1):
        cnt += size2
        flag += 1
    # 스티커 2개 여부 확인
    if flag == 2:
      if cnt > ans:
        ans = cnt
      flag -= 1
      cnt -= size2


print(ans)