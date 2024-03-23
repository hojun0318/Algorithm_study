from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    visited_bfs = [[0] * 5 for _ in range(5)]
    visited_bfs[x][y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + i
            ny = y + j

            if 0 <= nx < 5 and 0 <= ny < 5 and visited_bfs[nx][ny] == 0 and visited_7[nx][ny] == 1:
                queue.append((nx, ny))
                visited_bfs[nx][ny] = 1
                cnt += 1
        
    return cnt == 7

def check():
    for i in range(5):
        for j in range(5):
            if visited_7[i][j] == 1:
                return bfs(i, j)

def dfs(n, cnt, s_cnt):
    global ans
    if cnt > 7:
        return
    if n == 25:
        if cnt == 7 and s_cnt >= 4:
            if check():
                ans += 1
        return
    
    visited_7[n // 5][n % 5] = 1
    dfs(n + 1, cnt + 1, s_cnt + int(arr[n // 5][n % 5] == 'S'))
    visited_7[n // 5][n % 5] = 0
    dfs(n + 1, cnt, s_cnt)



arr = [list(map(str, input())) for _ in range(5)]
visited_7 = [[0] * 5 for _ in range(5)]
ans = 0

dfs(0, 0, 0)

print(ans)