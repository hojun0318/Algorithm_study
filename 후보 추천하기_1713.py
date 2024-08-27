from collections import deque

N = int(input())
S = int(input())
students = list(map(int, input().split()))

# 1. 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
vote = [0] * 105
queue = deque()

for i in range(S):
  # 2. 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
  if len(queue) < N:
    if students[i] not in queue:
      queue.append(students[i])
      vote[students[i]] += 1
    # 4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
    else:
      vote[students[i]] += 1
  # 3. 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다
  else:
    if students[i] not in queue:
      min_vote = 1001
      for n in queue:
        min_vote = min(min_vote, vote[n])
      
      flag = False
      for _ in range(N):
        chk = queue.popleft()
        if flag == False:
          if vote[chk] == min_vote:
            flag = True
            vote[chk] = 0
          else:
            queue.append(chk)
        
        elif flag == True:
          queue.append(chk)

      if flag == True:
        queue.append(students[i])
        vote[students[i]] += 1

    # 4. 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
    else:
      vote[students[i]] += 1

ans = []
for _ in range(len(queue)):
  ans.append(queue.popleft())

ans.sort()

print(*ans)