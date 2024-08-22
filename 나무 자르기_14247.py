N = int(input())
High = list(map(int, input().split()))
Growth = list(map(int, input().split()))
ans = 0

lst = [[0, 0]]
for i in range(N):
    lst.append([Growth[i], High[i]])

lst.sort()

for day in range(1, N + 1):
    ans += lst[day][1] + (lst[day][0] * (day - 1))

    
print(ans)