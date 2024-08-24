N, K = map(int, input().split())
num = list(map(int, input().split()))

lst = []

for i in range(N - 1):
  n = num[i+1] - num[i]
  lst.append(n)

lst.sort()
cost = 0

for i in range(N-K):
  cost += lst[i]

print(cost)