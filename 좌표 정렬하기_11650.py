N = int(input())
lst = []

for _ in range(N):
  lst.append(list(map(int, input().split())))

lst.sort()

for point in lst:
  print(*point)