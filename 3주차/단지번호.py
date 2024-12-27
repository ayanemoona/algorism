N=int(input())
lst=[]
corr=[]
visit=[[0]*N for i in range(N)]

def dfs(x,y):
    global max
    visit[x][y]=1
    max+=1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == '1' and not visit[nx][ny]:
            dfs(nx, ny)
    return max
for i in range(N):
    a=list(input())
    lst.append(a)
for i in range(N):
    for j in range(N):
        max=0
        if lst[i][j]=='1' and visit[i][j]==0:
            max=dfs(i,j)
            corr.append(max)
print(len(corr))  
corr.sort()         
for i in corr:
    print(i)
