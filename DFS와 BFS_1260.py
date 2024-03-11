from collections import deque
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

def dfs(v):
    dfs_visited[v] = 1
    print(v, end = ' ')

    graph[v].sort()
    for i in graph[v]:
        if dfs_visited[i] == 0:
            dfs(i)

def bfs(start):
    queue = deque([start])
    bfs_visited[start] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        graph[v].sort()

        for i in graph[v]:
            if bfs_visited[i] == 0:
                queue.append(i)
                bfs_visited[i] = 1


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)

dfs(v)
print()
bfs(v)