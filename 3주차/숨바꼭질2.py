from collections import deque

def bfs(n, k):
    # 방문 기록: 방문한 위치와 그 위치까지 걸린 시간을 기록
    visited = [-1] * 100001
    queue = deque([(n, 0)])  # (현재 위치, 걸린 시간)
    visited[n] = 0  # 시작 지점 시간 초기화

    min_time = float('inf')  # 최단 시간 초기화 (제일 큰 값)
    count = 0  # 최단 경로의 개수

    while queue: # 큐에 값이 있으면 반복
        current, time = queue.popleft()

        # 최단 시간을 초과하면 더 이상 탐색할 필요 없음
        if time > min_time:
            continue

        # 동생 위치에 도달한 경우
        if current == k:
            min_time = time  # 최단 시간 업데이트
            count += 1       # 최단 경로 개수 증가
            continue #bfs는 처음 나온 결과 값이  최단거리

        # 이동 가능한 경우의 수
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000:  # 범위 안에 있어야 함
                # 아직 방문하지 않았거나, 동일 시간에 방문 가능한 경우
                if visited[next_pos] == -1 or visited[next_pos] == time + 1:
                    visited[next_pos] = time + 1
                    queue.append((next_pos, time + 1))

    return min_time, count

# 입력
N, K = map(int, input().split())

# BFS 수행
min_time, count = bfs(N, K)

# 결과 출력
print(min_time)
print(count)
