import heapq

N = int(input())
M = int(input())
load = [[] for _ in range(N + 1)]

for _ in range(M):
  n1, n2, dis = map(int, input().split())
  load[n1].append([n2, dis])

s, e = map(int, input().split())

costs = [1e9 for _ in range(N + 1)]
costs[s] = 0

heap = []
heapq.heappush(heap, [0, s])

while heap:
  tot, node = heapq.heappop(heap)

  if costs[node] < tot:
    continue

  for nxt_node, nxt_cost in load[node]:
    sum_cost = tot + nxt_cost
    if sum_cost >= costs[nxt_node]:
      continue

    costs[nxt_node] = sum_cost
    heapq.heappush(heap, [sum_cost, nxt_node])

print(costs[e])