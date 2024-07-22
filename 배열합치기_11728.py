N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
aidx = bidx = 0

while aidx != N or bidx != M:
    if aidx == N:
        ans.append(B[bidx])
        bidx += 1
    elif bidx == M:
        ans.append(A[aidx])
        aidx += 1
    else:
        if A[aidx] < B[bidx]:
            ans.append(A[aidx])
            aidx += 1
        else:
            ans.append(B[bidx])
            bidx += 1
            
print(*ans)


# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# ans = sorted(A + B)

# print(*ans)
