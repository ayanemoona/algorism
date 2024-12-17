money = int(input())
lst = list(map(int, input().split()))

# BNP 전략
BNP = money
B_score = 0

for price in lst:
    if BNP // price > 0:
        B_score += BNP // price
        BNP %= price

B_result = BNP + (lst[-1] * B_score)

# TIMING 전략
TIMING = money
T_score = 0

for i in range(len(lst)):
    if i < 3:  # 첫 3일은 패턴을 확인할 수 없으므로 건너뜀
        continue
    
    # 연속 3일 상승
    if lst[i-3] < lst[i-2] < lst[i-1] < lst[i]:
        TIMING += lst[i] * T_score  # 주식 판매
        T_score = 0  # 보유 주식 수 초기화
    
    # 연속 3일 하락
    elif lst[i-3] > lst[i-2] > lst[i-1] > lst[i]:
        T_score += TIMING // lst[i]  # 주식 구매
        TIMING %= lst[i]  # 남은 돈 갱신

T_result = TIMING + (lst[-1] * T_score)

# 결과 비교
if B_result > T_result:
    print("BNP")
elif B_result < T_result:
    print("TIMING")
else:
    print("SAMESAME")
