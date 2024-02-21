stick = input()

ans = cnt = 0

for s in range(len(stick)):
  if stick[s] == '(':
    cnt += 1
  else:
    cnt -= 1
    if stick[s - 1] == '(':
      ans += cnt
    else:
      ans += 1

print(ans)