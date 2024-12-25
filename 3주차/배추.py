import sys
sys.setrecursionlimit(10**6)
T=int(input())
def dfs(x,y):
    visit[x][y]=1

# 상, 하, 좌, 우 탐색
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        # 좌표가 유효하고, 배추가 있으며, 방문하지 않았다면 DFS 호출
        if 0 <= nx < M and 0 <= ny < N and lst[nx][ny] == 1 and not visit[nx][ny]:
            dfs(nx, ny)
    
for i in range(T):
    M,N,K=map(int,input().split())
    lst=[[0]*N for i in range(M)]
    visit=[[0]*N for i in range(M)]
    corr = 0  # 컴포넌트 개수 저장
    for i in range(K):
        X,Y=map(int,input().split())
        lst[X][Y]=1
    for i in range(M):
        for j in range(N):
            # 배추가 있고 방문하지 않았다면 새로운 컴포넌트 시작
            if lst[i][j] == 1 and not visit[i][j]:
                dfs(i, j)  # 연결된 모든 배추를 탐색
                corr += 1  # 컴포넌트 개수 증가

    # 결과 출력
    print(corr)

    