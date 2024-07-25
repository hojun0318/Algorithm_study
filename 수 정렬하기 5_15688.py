N = int(input())
lst = [0] * 2000001

for _ in range(N):
  n = int(input())
  lst[n + 1000000] += 1

for i in range(2000001):
  while lst[i]:
    print(i - 1000000)
    lst[i] -= 1