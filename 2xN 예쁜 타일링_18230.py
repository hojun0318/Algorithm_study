N, A, B = map(int, input().split()) 
lst2_1 = sorted(list(map(int, input().split()))) 
lst2_2 = sorted(list(map(int, input().split())))    
ans = 0 

if N % 2 == 1: 
  ans += lst2_1[-1] 
  lst2_1.pop(-1) 
  N -= 1 

for _ in range(0, N, 2): 
  t1, t2 = 0, 0 
  if len(lst2_1) >= 2: 
    t1 = lst2_1[-1] + lst2_1[-2] 
  if len(lst2_2) >= 1: 
    t2 = lst2_2[-1] 
        
  if t1 > t2: 
    ans += t1 
    lst2_1.pop()
    lst2_1.pop() 
  else: 
    ans += t2 
    lst2_2.pop() 

print(ans)