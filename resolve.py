# import sys
# sys.stdin = open("input.txt", "r")

def dfs(n, cnt):
  global ans

  if ans >= (cnt + (N - n) * 2):
    return

  if n == N:
    ans = max(ans, cnt)
    return
  
  if eggs[n][0] <= 0:
    dfs(n + 1, cnt)
  
  else:
    flag = False

    for i in range(N):
      if i == n or eggs[i][0] <= 0:
        continue

      flag = True
      eggs[n][0] -= eggs[i][1]
      eggs[i][0] -= eggs[n][1]

      dfs(n + 1, cnt + int(eggs[n][0] <= 0) + int(eggs[i][0] <= 0))

      eggs[n][0] += eggs[i][1]
      eggs[i][0] += eggs[n][1]
    
    if flag == False:
      dfs(n + 1, cnt)



N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(0, 0)

print(ans)