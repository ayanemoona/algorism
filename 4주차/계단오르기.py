def max_score(stairs):
    n = len(stairs)
    if n == 1:
        return stairs[0]  # 계단이 하나일 때
    if n == 2:
        return stairs[0] + stairs[1]  # 계단이 두 개일 때

    # DP 배열 초기화
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    # DP 점화식 계산
    for i in range(3, n):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    return dp[-1]  # 마지막 계단의 최대 점수

# 입력 받기
n = int(input())
stairs = [int(input()) for _ in range(n)]

# 결과 출력
print(max_score(stairs))
