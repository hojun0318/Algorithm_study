from collections import deque

A, B, C = map(int, input().split())
visited = [[0] * (B + 1) for _ in range(A + 1)]

queue = deque()

ans = []

def remain(na, nb):
  if not visited[na][nb]:
    visited[na][nb] = 1
    queue.append((na, nb))
        
def pour(a, b):
  queue.append((a, b))
  visited[0][0] = 1

  while queue:
    a, b = queue.popleft()
    c = C - a - b
    
    # A물통에 물이 없을때 C물통의 물의 양
    if a == 0:
        ans.append(c)
        
    w = min(a, B - b)         # A -> B 옮길 물의 양
    remain(a - w, b + w)        # 옮긴 후의 a와 b의 물의 양

    w = min(a, C - c)         # A -> C
    remain(a - w, b)
    
    w = min(b, C - c)         # B -> C
    remain(a, b - w)
    w = min(b, A - a)         # B -> A
    remain(a + w, b - w)
    
    w = min(c, A - a)         # C -> A
    remain(a + w, b)
    w = min(c, B - b)         # C -> B
    remain(a, b + w)
        

pour(0, 0)

ans.sort()

print(*ans)