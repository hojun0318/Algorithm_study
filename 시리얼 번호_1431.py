N = int(input())
lst = []

for _ in range(N):
  tmp = []
  num = 0
  word = input()
  len_word = len(word)
  tmp.append(word)
  tmp.append(len_word)

  for i in range(len_word):
    if 'a' <= word[i] <= 'z' or 'A' <= word[i] <= 'Z':
      continue
    if 0 <= int(word[i]) <= 9:
      num += int(word[i])
    
    
  tmp.append(num)
  lst.append(tmp)

lst.sort(key = lambda x : (x[1], x[2], x[0]))

for w in lst:
  print(w[0])