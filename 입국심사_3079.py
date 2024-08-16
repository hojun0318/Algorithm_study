def Count(mid):
  cnt = 0

  for i in range(N):
    cnt += mid // lst[i]

  return cnt


N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
ans = min(lst) * M

s = 1
e = max(lst) * M

while s <= e:
  mid = (s + e) // 2

  if Count(mid) >= M:
    e = mid - 1
    ans = min(ans, mid)
  else:
    s = mid + 1

print(ans)