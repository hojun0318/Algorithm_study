import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, res):
  visited[x] = 1
  cycle.append(x) # 사이클을 이루는 팀을 확인하기 위함
  nx = choice[x]

  if visited[nx]: # 방문 가능한 곳이 끝났는지
    if nx in cycle: # 사이클 가능 여부
      res += cycle[cycle.index(nx) : ]  # 사이클 되는 구간부터만 팀을 이룸
    return
  else:
    dfs(nx, res)



for _ in range(int(input())):
  n = int(input())
  choice = [0] + list(map(int, input().split()))
  visited = [0] * (n + 1)
  res = []

  for i in range(1, n + 1):
    if not visited[i]:  # 방문하지 않은 곳이라면
      cycle = []
      dfs(i, res)

  print(n - len(res))   # 팀에 없는 사람 수