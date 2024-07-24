N = int(input())
lst = []

for _ in range(N):
  n = int(input())
  lst.append(n)

lst = sorted(lst)

cursor = lst[0]
cnt = 1
mxcnt = ans = 0

for i in range(1, N):
  if cursor == lst[i]:
    cnt += 1
  else:
    if cnt > mxcnt:
      mxcnt = cnt
      ans = cursor
    
    cursor = lst[i]
    cnt = 1
    
if cnt > mxcnt:
  mxcnt = cnt
  ans = cursor

print(ans)