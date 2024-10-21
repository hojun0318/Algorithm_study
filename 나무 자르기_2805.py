def mx_height(height):
  tmp = 0
  for tree in lst:
    if tree - height > 0:
      tmp += (tree - height)

  if tmp >= M:
    return True
  else:
    return False


N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)
ans = 0

while start <= end:
  mid = (start + end) // 2

  if mx_height(mid):
    ans = mid
    start = mid + 1

  else:
    end = mid - 1

print(ans)