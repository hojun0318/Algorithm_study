import sys

N = int(input())
lst = []

for _ in range(N):
  word = sys.stdin.readline().strip()
  len_word = len(word)
  if [len_word, word] in lst:
    continue
  else:
    lst.append([len_word, word])

lst.sort(key = lambda x : (x[0], x[1]))

for i in range(len(lst)):
  print(lst[i][1])