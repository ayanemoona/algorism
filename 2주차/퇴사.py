def simulate(day, total):
    global max_profit

    # 퇴사일을 넘으면 종료
    if day > N:
        max_profit = max(max_profit, total)
        return

    # 상담을 선택하지 않는 경우
    simulate(day + 1, total)

    # 상담을 선택할 수 있는 경우
    if day + T[day - 1] <= N + 1:
        simulate(day + T[day - 1], total + P[day - 1])

# 입력 처리
N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

max_profit = 0

# 시뮬레이션 시작
simulate(1, 0)

print(max_profit)
