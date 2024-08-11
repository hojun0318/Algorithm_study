from collections import deque

A, B, C = map(int, input().split())

# 경우의 수를 담을 큐
queue = deque()
queue.append((0, 0))

# 방문 여부 저장
visited = [[0] * (B + 1) for _ in range(A + 1)]
visited[0][0] = 1

ans = []

def pour(x, y):
  if not visited[x][y]:
    visited[x][y] = True
    queue.append((x, y))
        
def bfs():
  while queue:
    # A물통에 있는 물: x, B물통에 있는 물: y, C물통에 있는 물: z
    x, y = queue.popleft()
    z = C - x - y
    
    # A 물통이 비어있는 경우에 C 물통에 남아있는 양 저장
    if x == 0:
        ans.append(z)
        
    # A에서 B로 물 이동
    water = min(x, B - y)
    pour(x - water, y + water)
    # A에서 C로 물 이동
    water = min(x, C - z)
    pour(x - water, y)
    
    # B에서 C로 물 이동
    water = min(y, C - z)
    pour(x, y - water)
    # B에서 A로 물 이동
    water = min(y, A - x)
    pour(x + water, y - water)
    
    # C에서 A로 물 이동
    water = min(z, A - x)
    pour(x + water, y)
    # C에서 B로 물 이동
    water = min(z, B - y)
    pour(x, y + water)
        
bfs()

ans.sort()

print(*ans)