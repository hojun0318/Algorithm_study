def dfs(n, lst):
  global cnt, tmp
  if n == L and cnt > 0 and tmp > 1:
    ans.append(lst)
    return
  
  for i in range(C):
    if lst:
      if not visited[i] and lst[-1] < st[i]:
        if st[i] in mohmm:
          cnt += 1
          visited[i] = 1
          dfs(n + 1, lst + [st[i]])
          visited[i] = 0
          cnt -= 1
        else:
          tmp += 1
          visited[i] = 1
          dfs(n + 1, lst + [st[i]])
          visited[i] = 0
          tmp -= 1
    else:
      if not visited[i]:
        if st[i] in mohmm:
          cnt += 1
          visited[i] = 1
          dfs(n + 1, lst + [st[i]])
          visited[i] = 0
          cnt -= 1
        else:
          tmp += 1
          visited[i] = 1
          dfs(n + 1, lst + [st[i]])
          visited[i] = 0
          tmp -= 1


L, C = map(int, input().split())
st = sorted(list(map(str, input().split())))

mohmm = ['a', 'e', 'i', 'o', 'u']
cnt = tmp = 0
ans = []
visited = [0] * C

dfs(0, [])

for lst in ans:
  res = ''
  for s in lst:
    res += s
  print(res)