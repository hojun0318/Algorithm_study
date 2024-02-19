import sys
sys.stdin = open("input.txt", "r")

str = input()
arr = [0] * 27

for i in str:
  arr[ord(i) - 97] += 1

for j in range(len(arr)):
    print(arr[j], end=" ")