S = input()
lst = []

for i in range(len(S)):
    lst.append(S[i:])

lst.sort()

for ans in lst:
    print(ans)