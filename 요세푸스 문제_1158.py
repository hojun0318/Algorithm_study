N, K = map(int, input().split())

table = [i for i in range(1, N + 1)]
delete = []
num = 0

for _ in range(N):
  num += K - 1
  if num >= len(table):
    num = num % len(table)

  delete.append(str(table.pop(num)))


print("<",", ".join(delete)[:],">", sep='')