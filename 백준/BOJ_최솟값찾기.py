N,L = map(int,input().split())
A = list(map(int,input().split()))
result = []
for i in range(L-1):
    A.insert(0,5000000)
for i in range(N):
    min = 5000000
    for j in range(L):
        if(A[i+j] < min):
            min = A[i+j]
    result.append(min)
    
print(*result)

