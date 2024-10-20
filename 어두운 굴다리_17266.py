N = int(input())
M = int(input())
lst = list(map(int, input().split()))

def canLight(height):
  if height - lst[0] < 0:
    return False
  
  for i in range(1, M):
    if lst[i] - lst[i - 1] > height * 2:
      return False
  
  if N - lst[-1] > height:
    return False
  
  return True


start = 1
end = ans = N

while start <= end:
  mid = (start + end) // 2

  if canLight(mid):
    ans = mid
    end = mid - 1

  else:
    start = mid + 1

print(ans)