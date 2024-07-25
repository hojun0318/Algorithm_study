N = int(input())
lst = []

for idx in range(N):
    age, name = map(str, input().split())
    lst.append([int(age), idx, name])
  

lst.sort()    

for a, i, n in lst:
    print(a, n)