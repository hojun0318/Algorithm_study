from queue import PriorityQueue

N = int(input())
M = int(input())
load = [[] for _ in range(N + 1)]

for _ in range(M):
  n1, n2, dis = map(int, input().split())
  load[n1].append([n2, dis])

s, e = map(int, input().split())

costs = [1e9 for _ in range(N + 1)]
costs[s] = 0

queue = PriorityQueue()
queue.put((0, s))

while True:
  if queue.empty():
    break
  
  tot, node = queue.get()
  
  if costs[node] < tot:
    continue

  for nxt_node, nxt_cost in load[node]:
    sum_cost = tot + nxt_cost
    if sum_cost >= costs[nxt_node]:
      continue

    costs[nxt_node] = sum_cost
    queue.put((sum_cost, nxt_node))

print(costs[e])