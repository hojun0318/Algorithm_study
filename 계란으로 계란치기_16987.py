def dfs(n, cnt):
  global ans
  if ans >= (cnt + (N - n) * 2):  # 끝까지 진행해도 최댓값보다 작으면
    return
  
  if n == N:                      # 모든 계란을 손에 들고 부딪히기 완료
    ans = max(ans, cnt)
    return
  
  if eggs[n][0] <= 0:             # 현재 계란이 깨진 경우 -> 다음 계란으로
    dfs(n + 1, cnt)
  else:                           # 현재 계란 안깨진 상태
    flag = False                  # 한번도 안 부딪혔다면 그래도 다음 계란으로 가야됨

    for i in range(N):            # 하나씩 부딪혀보기
      if n == i or eggs[i][0] <= 0:
        continue
      flag = True

      eggs[n][0] -= eggs[i][1]
      eggs[i][0] -= eggs[n][1]
      
      dfs(n + 1, cnt + int(eggs[n][0] <= 0) + int(eggs[i][0] <= 0))
      
      eggs[n][0] += eggs[i][1]
      eggs[i][0] += eggs[n][1]

    if flag == False:
      dfs(n + 1, cnt)

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = 0

dfs(0, 0)                         # 계란 index, 깨진 계란의 갯수

print(ans)