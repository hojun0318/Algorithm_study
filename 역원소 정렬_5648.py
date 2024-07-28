lst = []
lst += input().split()

ans = []
flag = True

while flag:
  lst += input().split()

  if len(lst) == int(lst[0]) + 1:
    flag = False

for i in range(1, int(lst[0]) + 1):
  tmp = int(lst[i][::-1])
  ans.append(tmp)

ans.sort()

for num in ans:
  print(num)