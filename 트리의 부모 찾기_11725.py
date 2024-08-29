from collections import deque

def bfs():
  queue = deque()
  queue.append((1))

  while queue:
    n = queue.popleft()
    for i in tree[n]:
      if top_node[i] == -1:
        top_node[i] = n
        queue.append((i))


N = int(input())
tree = [[] for _ in range(N + 1)]
top_node = [-1] * (N + 1)

for _ in range(N - 1):
  n1, n2 = map(int, input().split())
  tree[n1].append(n2)
  tree[n2].append(n1)

bfs()

for i in range(2, N + 1):
  print(top_node[i])