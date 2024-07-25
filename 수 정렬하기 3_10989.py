N = int(input())
lst = [0] * 10001

for _ in range(N):
    n = int(input())
    lst[n] += 1
    
    
for i in range(10001):
    while lst[i]:
        print(i)
        lst[i] -= 1