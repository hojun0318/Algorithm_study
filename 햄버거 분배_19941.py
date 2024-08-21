N, K = map(int, input().split())
lst = list(map(str, input()))
ans = []

for i in range(N):
  if lst[i] == 'P':
    for j in range(i - K, i + (K + 1)):
      if 0 <= j < N:
        if lst[j] == 'H':
          ans.append([i, j])
          lst[j] = 'X'
          break

print(len(ans))