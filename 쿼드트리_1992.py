N = int(input())
tree = [list(map(int, input())) for _ in range(N)]
ans = []

def quadtree(x, y, n):
  color = tree[x][y]

  for i in range(x, x + n):
    for j in range(y, y + n):
      if color != tree[i][j]:
        ans.append('(')
        for k in range(2):
          for l in range(2):
            quadtree(x + k * n // 2, y + l * n // 2, n // 2)
        ans.append(')')
        return
      
  ans.append(color)




quadtree(0, 0, N)

for i in ans:
  print(i, end = '')