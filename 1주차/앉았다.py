from itertools import combinations

def calculate_win_probability(A, B):
    # 전체 카드 덱 생성 (1부터 10까지 각 2장씩)
    deck = [i for i in range(1, 11)] * 2

    # 영학이의 패를 덱에서 제거
    deck.remove(A)
    deck.remove(B)

    # 족보 계산 함수 정의
    def calculate_score(cards):
        if cards[0] == cards[1]:
            return 100 + cards[0]  # 땡의 경우 100 이상의 점수로 처리
        else:
            return (cards[0] + cards[1]) % 10  # 끗의 경우 합의 일의 자리 계산

    # 영학이의 족보 점수 계산
    yeonghak_score = calculate_score([A, B])

    # 상대방이 가질 수 있는 모든 패 조합 생성
    opponent_hands = list(combinations(deck, 2))

    # 영학이가 이길 수 있는 경우의 수 계산
    win_count = 0
    for opp_hand in opponent_hands:
        opp_score = calculate_score(opp_hand)
        if yeonghak_score > opp_score:
            win_count += 1

    # 총 가능한 경우의 수
    total_cases = len(opponent_hands)

    # 승리 확률 계산
    win_probability = win_count / total_cases

    # 결과 출력 (소수점 셋째 자리까지 반올림)
    return f"{win_probability:.3f}"

# 입력 받기
A, B = map(int, input().split())
print(calculate_win_probability(A, B))
