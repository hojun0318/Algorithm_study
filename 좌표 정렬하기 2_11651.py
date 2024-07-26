N = int(input())
lst = []

for _ in range(N):
  lst.append(list(map(int, input().split())))

lst.sort(key = lambda x : (x[1], x[0]))

for point in lst:
  print(*point)