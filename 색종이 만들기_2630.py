N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

zero = 0
one = 0

def dfs(x, y, n):
  global zero, one

  current_color = papers[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if papers[i][j] != current_color:
        for k in range(2):
          for l in range(2):
            dfs(x + k * n //2, y + l * n // 2, n // 2)
        return
      
  if current_color == 0:
    zero += 1
  else:
    one += 1

dfs(0, 0, N)

print(zero)
print(one)