def Count(capacity):
  # 블루레이 최소 1장 필요
  cnt = 1
  # 블루레이 1장에 저장되는 곡 합
  sum = 0

  for m in music:
    # (초과) 현재 저장된 곡의 시간 + 추가될 곡의 시간 > 용량
    if sum + m > capacity:
      # 새로운 블루레이 추가
      cnt += 1
      # 새로 저장
      sum = m
    # (미만)
    else:
      sum += m

  return cnt


N, M = map(int, input().split())
music = list(map(int, input().split()))
mx = max(music)

s = 1
e = sum(music)
ans = 0

while s <= e:
  capacity = (s + e) // 2

  # 용량은 플레이리스트 중 긴 곡보다 같거나 커야하고, 블루레이 개수가 M 이하라면
  if capacity >= mx and Count(capacity) <= M:
    ans = capacity
    # 더 큰 용량은 만족하니까 -> 최소값 찾기
    e = capacity - 1
  # 블루레이 개수가 M 초과라면
  else:
    # 용량 증가
    s = capacity + 1

print(ans)