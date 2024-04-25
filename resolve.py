N = int(input())

obN = list(bin(N)[2:][::-1])
t, ans = 1, 0

for i in obN:
  ans += int(i) * t
  t *= 3

print(ans)