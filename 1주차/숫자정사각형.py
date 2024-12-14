N,M=map(int,input().split())
lst=[]
for i in range(N):
    a=list(input())
    lst.append(a)

max_size = min(N, M)
max_square = 1  
for n in range(max_size, 0, -1):
    for i in range(N - n + 1):
        for j in range(M - n + 1):
            if lst[i][j] == lst[i][j + n - 1] == lst[i + n - 1][j] == lst[i + n - 1][j + n - 1]:
                max_square = n
                break
        if max_square == n:
            break
    if max_square == n:
        break


print(max_square * max_square)


