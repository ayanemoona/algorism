N = int(input())

# 생성자를 찾는 함수
def find_constructor(N):
    for M in range(1, N + 1):
        # 분해합 계산
        digit_sum = sum(int(d) for d in str(M))  # M의 각 자리수 합
        if M + digit_sum == N:  # 분해합이 N과 같은지 확인
            return M  # 가장 작은 생성자 반환
    return 0  # 생성자가 없으면 0 반환

# 결과 출력
print(find_constructor(N))