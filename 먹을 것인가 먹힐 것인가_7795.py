T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  A.sort()
  B.sort()

  ans = 0
  for a in A:
    if a == 1:
      continue
    if a > B[-1]:
      ans += len(B)
    else:
      for i in range(len(B)):
        if a <= B[i]:
          ans += i
          break

  print(ans)