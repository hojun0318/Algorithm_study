N, C = map(int, input().split())
lst = list(map(int, input().split()))

tmp = []

for n in lst:
  if n not in tmp:
    tmp.append(n)

arr = [[0] * 3 for _ in range(len(tmp))]

for idx, num in enumerate(tmp):
  cnt = 0
  for j in lst:
    if j == num:
      cnt += 1

  arr[idx][0] = -cnt    
  arr[idx][1] = idx + 1
  arr[idx][2] = num

arr.sort(key = lambda x : (x[0], x[1]))


ans = []

for i in arr:
  for j in range(-i[0]):
    ans.append(i[2])

print(*ans)