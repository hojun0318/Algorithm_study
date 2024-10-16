from itertools import permutations
from collections import deque

N = int(input())
num = deque(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(N):
  T, S, B = map(int, input().split())
  T = list(str(T))

  for i in range(len(num)):
    s_cnt = b_cnt = 0
    tmp = num.popleft()

    for j in range(3): 
      if int(T[j]) in tmp:
        if j == tmp.index(int(T[j])):
          s_cnt += 1
        else:
          b_cnt += 1
    
    if s_cnt == S and b_cnt == B:
      num.append(tmp)


print(len(num))