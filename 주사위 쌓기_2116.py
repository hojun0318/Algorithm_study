# from collections import deque

# N = int(input())
# dices = []

# for _ in range(N):
#   dices.append(list(map(int, input().split())))

# queue = deque()
# ans = 0

# for idx in range(3):
#   if idx == 0:
#     t, b = dices[0][idx], dices[0][-1]
#     queue.append((t, b))
#     queue.append((b, t))
#   elif idx == 1:
#     t, b = dices[0][idx], dices[0][idx + 2]
#     queue.append((t, b))
#     queue.append((b, t))
#   else:
#     t, b = dices[0][idx], dices[0][idx + 2]
#     queue.append((t, b))
#     queue.append((b, t))
        
# print(queue)



# while queue:
#   res = 0
#   t, b = queue.popleft()

#   print('t, b : ', t, b)

#   for dice in range(N):
#     tmp = 0

#     if dice == 0:
#       for num in dices[dice]:
#         if num not in [t, b]:
#           tmp = max(tmp, num)

#       print('max : ', tmp)
#       res += tmp

#     if dice != 0:
#       for i in range(N):
#         if t == dices[dice][i]:
#           if i == 0:
#             nt, nb = dices[dice][-1], dices[dice][0]
#           elif i == 1:
#             nt, nb = dices[dice][i + 2], dices[dice][i]
#           elif i == 2:
#             nt, nb = dices[dice][i + 2], dices[dice][i]
#           elif i == 3:
#             nt, nb = dices[dice][i - 2], dices[dice][i]
#           elif i == 4:
#             nt, nb = dices[dice][i - 2], dices[dice][i]
#           elif i == 5:
#             nt, nb = dices[dice][0], dices[dice][5]
          
#       t, b = nt, nb

#       for num in dices[dice]:
#         if num not in [nt, nb]:
#           tmp = max(tmp, num)

#       print('nt, nb : ', t, b)
#       print('max : ', tmp)
#       res += tmp
#   print('------------------------------------------')

#   ans = max(ans, res)
    
# print(ans)


from collections import deque

N = int(input())
dices = []

for _ in range(N):
  dices.append(list(map(int, input().split())))

queue = deque()
ans = 0

for idx in range(3):
  if idx == 0:
    t, b = dices[0][idx], dices[0][-1]
    queue.append((t, b))
    queue.append((b, t))
  elif idx == 1:
    t, b = dices[0][idx], dices[0][idx + 2]
    queue.append((t, b))
    queue.append((b, t))
  else:
    t, b = dices[0][idx], dices[0][idx + 2]
    queue.append((t, b))
    queue.append((b, t))


while queue:
  res = 0
  t, b = queue.popleft()

  for dice in range(N):
    tmp = 0

    if dice == 0:
      for num in dices[dice]:
        if num not in [t, b]:
          tmp = max(tmp, num)

      res += tmp

    if dice != 0:
      for i in range(6):
        if t == dices[dice][i]:
          if i == 0:
            nt, nb = dices[dice][-1], dices[dice][0]
          elif i == 1:
            nt, nb = dices[dice][i + 2], dices[dice][i]
          elif i == 2:
            nt, nb = dices[dice][i + 2], dices[dice][i]
          elif i == 3:
            nt, nb = dices[dice][i - 2], dices[dice][i]
          elif i == 4:
            nt, nb = dices[dice][i - 2], dices[dice][i]
          elif i == 5:
            nt, nb = dices[dice][0], dices[dice][5]
          
      t, b = nt, nb

      for num in dices[dice]:
        if num not in [nt, nb]:
          tmp = max(tmp, num)
          
      res += tmp

  ans = max(ans, res)
    
print(ans)