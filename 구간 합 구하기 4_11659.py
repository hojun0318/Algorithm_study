N, M = map(int, input().split())
arr = list(map(int, input().split()))

lst = [0]
sm = 0

for i in range(N):
  sm += arr[i]
  lst.append(sm)

for j in range(M):
  s, e = map(int, input().split())
  print(lst[e] - lst[s - 1])