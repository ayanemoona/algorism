def dfs(idx, current_value, add, sub, mul, div):
    global max_value, min_value

    if idx == n:  # 모든 숫자를 다 사용한 경우
        max_value = max(max_value, current_value)
        min_value = min(min_value, current_value)
        return

    # 각 연산자를 하나씩 사용해 재귀적으로 탐색
    if add > 0:
        dfs(idx + 1, current_value + numbers[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, current_value - numbers[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, current_value * numbers[idx], add, sub, mul - 1, div)
    if div > 0:
        dfs(idx + 1, int(current_value / numbers[idx]), add, sub, mul, div - 1)

# 입력 받기
n = int(input())  # 숫자의 개수
numbers = list(map(int, input().split()))  # 숫자 리스트
add, sub, mul, div = map(int, input().split())  # 각 연산자의 개수

# 결과 초기화
max_value = -float('inf')  # 초기 최대값
min_value = float('inf')   # 초기 최소값

# DFS 시작
dfs(1, numbers[0], add, sub, mul, div)

# 결과 출력
print(max_value)
print(min_value)
