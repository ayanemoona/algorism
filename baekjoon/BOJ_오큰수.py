N = int(input())
A = list(map(int,input().split()))
result = [0]*N
for i in range(N):
    for j in range(i+1,N):
         if A[i] < A[j]:
            result[i]=A[j]
            break
    if(result[i] == 0):
        result[i] = -1

print(*result)