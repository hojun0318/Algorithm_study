# T = int(input())

# for _ in range(T):
#   n, m = map(int, input().split())
#   A = list(map(int, input().split()))
#   B = list(map(int, input().split()))
#   B.sort()
#   C = []


#   for i in range(n):
#     mn = 1000000001
#     ans = 0
#     sub = 0
#     for j in range(m):
#       sub = abs(A[i] - B[j])

#       if mn > sub:
#         mn = sub
#         ans = B[j]

#     C.append(ans)
  
#   print(sum(C))
N = 16
lst = list(map(int, input().split()))
lst.sort()
print(lst)
s = 0
e = len(lst)

while True:
  