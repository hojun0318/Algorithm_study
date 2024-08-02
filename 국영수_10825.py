N = int(input())
lst = []

for _ in range(N):
    name, korea, english, math = map(str, input().split())
    lst.append([-int(korea), int(english), -int(math), name])
    
lst.sort(key = lambda x : (x[0], x[1], x[2], x[3]))

for i in range(N):
    print(lst[i][3])