N, K = map(int, input().split())
height = sorted(list(map(int, input().split())))

lst = []

for i in range(N - 1):
  n = height[i + 1] - height[i]
  lst.append(n)

lst.sort()
cost = 0

for i in range(N - K):
  cost += lst[i]

print(cost)