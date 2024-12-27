from collections import deque

def bfs(start, target):
    if start == target:
        return 0  # 이미 같은 위치에 있다면 이동 필요 없음
    
    visited = [False] * 100001  # 방문 체크
    queue = deque([(start, 0)])  # (현재 위치, 이동 횟수)
    visited[start] = True
    
    while queue:
        current, count = queue.popleft()
        
        # 다음 위치로 이동
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                if next_pos == target:
                    return count + 1  # 목표 위치에 도달했을 경우
                visited[next_pos] = True
                queue.append((next_pos, count + 1))
    
    return -1  # 문제 조건상 여기에 도달하지 않음

# 입력 처리
N, K = map(int, input().split())
print(bfs(N, K))
