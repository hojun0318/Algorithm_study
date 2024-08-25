N, A, B = map(int, input().split())
a_2x1 = sorted(list(map(int, input().split())))
b_2x2 = sorted(list(map(int, input().split())))

ans = 0

if N % 2 == 1:
  ans += a_2x1[-1]
  a_2x1.pop()
  N -= 1

for _ in range(0, N, 2):
  tile_A, tile_B = 0, 0
  if len(a_2x1) >= 2:
    tile_A = a_2x1[-1] + a_2x1[-2]
  if len(b_2x2) >= 1:
    tile_B = b_2x2[-1]

  if tile_A > tile_B:
    ans += tile_A    
    for _ in range(2):
      a_2x1.pop()
  else:
    ans += tile_B
    b_2x2.pop()


print(ans)