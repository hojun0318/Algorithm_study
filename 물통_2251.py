from collections import deque

A, B, C = map(int, input().split())
visited = [[0] * (B + 1) for _ in range(A + 1)]

queue = deque()

ans = []

def pour(a, b):
  if not visited[a][b]:
    visited[a][b] = 1
    queue.append((a, b))
        
def bfs(a, b):
  queue.append((a, b))
  visited[0][0] = 1

  while queue:
    a, b = queue.popleft()
    c = C - a - b
    
    # A물통에 물이 없을때 C물통의 물의 양
    if a == 0:
        ans.append(c)
        
    w = min(a, B - b)         # A -> B 옮길 물의 양
    pour(a - w, b + w)        # 옮긴 후의 a와 b의 물의 양

    w = min(a, C - c)         # A -> C
    pour(a - w, b)
    
    w = min(b, C - c)         # B -> C
    pour(a, b - w)
    w = min(b, A - a)         # B -> A
    pour(a + w, b - w)
    
    w = min(c, A - a)         # C -> A
    pour(a + w, b)
    w = min(c, B - b)         # C -> B
    pour(a, b + w)
        

bfs(0, 0)

ans.sort()

print(*ans)