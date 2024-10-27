N = int(input())
words = [str(input()) for _ in range(N)]
keyword = []
ans = []

for word in words:
  tmp = []
  key = ''
  for idx in range(len(word)):
    if word[idx] == ' ':
      if key:
        tmp.append(key)
        key = ''
    else:
      key += word[idx]

  tmp.append(key)
  flag = False

  buffer = ''
  for i in range(len(tmp)):
    if flag == True:
      buffer += ' '
      buffer += tmp[i]
    
    else:
      if tmp[i][0] not in keyword:
        if tmp[i][0].islower():
          keyword.append(tmp[i][0])
          keyword.append(tmp[i][0].upper())
        else:
          keyword.append(tmp[i][0])
          keyword.append(tmp[i][0].lower())
        
        if i == 0:
          buffer += '[' + tmp[i][0] + ']' + tmp[i][1:]
        else:
          buffer += ' '
          buffer += '[' + tmp[i][0] + ']' + tmp[i][1:]

        flag = True

      else:
        if i != 0:
          buffer += ' '
          buffer += tmp[i]
        else:
          buffer += tmp[i]

  if flag == False:
    buffer = ''

    for j in range(len(tmp)):
      chk = tmp[j][0]
      if flag == True:
        buffer += ' '
        buffer += tmp[j]

      else:
        for k in range(1, len(tmp[j])):
          if tmp[j][k] not in keyword:
            if tmp[j][k].islower():
              keyword.append(tmp[j][k])
              keyword.append(tmp[j][k].upper())
            else:
              keyword.append(tmp[j][k])
              keyword.append(tmp[j][k].lower())
          
            if j == 0:
              buffer += tmp[j][:k] + '[' + tmp[j][k] + ']' + tmp[j][k + 1:]
            else:
              buffer += ' '
              buffer += tmp[j][:k] + '[' + tmp[j][k] + ']' + tmp[j][k + 1:]
              
            flag = True
            break
          
          else:
            chk += tmp[j][k]
        
        if chk == tmp[j]:
          if j == 0:
            buffer += chk
          else:
            buffer += ' '
            buffer += chk


  if flag == True:
    ans.append(buffer)
  if flag == False:
    ans.append(word)

for res in ans:
  print(res)