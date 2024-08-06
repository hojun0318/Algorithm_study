def dfs(n, tot, cnt):
  global ans

  # 3번, 종료조건 설정
  if n == N:
    # 조건1 : 해당 부분수열의 합이 S인가, 조건2: 크기가 양수인가(최소 1개 이상)
    if tot == S and cnt > 0:
      ans += 1
    return
  
  # 2진 트리(2^20 약 10^6)
  # 5번 해당 숫자를 포함하는 경우 / 포함하지 않는 경우
  dfs(n + 1, tot + lst[n], cnt + 1)
  dfs(n + 1, tot, cnt)

# 1번, 입력 받기
N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

# 2번, n을 인덱스로 설정하고, N - 1까지 즉, 이진트리 말단 노드까지 탐색
dfs(0, 0, 0)

print(ans)