def make_one(n):
    dp = [0] * (n + 1)  # dp 테이블 초기화
    
    for i in range(2, n + 1):
        # 기본적으로 i-1에서 오는 경우를 생각
        dp[i] = dp[i - 1] + 1
        
        # i가 2로 나누어떨어질 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # i가 3으로 나누어떨어질 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]

# 예시 실행
n = int(input())
print(make_one(n))
