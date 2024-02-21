# import sys
# sys.stdin = open("input.txt", "r")

from sys import stdin

left = list(input())
right = []

for _ in range(int(input())):
  cursor = list(stdin.readline().split())
  if cursor[0] == 'L' and left:
    right.append(left.pop())
  elif cursor[0] == 'D' and right:
    left.append(right.pop())
  elif cursor[0] == 'B' and left:
    left.pop()
  elif cursor[0] == 'P':
    left.append(cursor[1])

ans = left + right[::-1]
print(''.join(ans))