N = int(input())
lst = list(map(int, input().split()))

start = 0
end = N - 1
ans = float("INF")
x, y = 0, N - 1

while start < end:
  sm = lst[start] + lst[end]

  if abs(sm) <= abs(ans):
    ans = sm
    x, y = start, end

  if sm == 0:
    break

  elif sm <= 0:
    start += 1

  else:
    end -= 1

print(lst[x], lst[y])