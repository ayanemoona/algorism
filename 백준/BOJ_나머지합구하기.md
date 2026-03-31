📝 문제 풀이 보고서: 백준 10986 (나머지 합)1. 문제 설명핵심 목표: 수 N개가 주어졌을 때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하기.조건: 구간 $[i, j]$의 합이 $M$으로 나누어 떨어져야 함. 즉, $(S[j] - S[i-1]) \pmod M = 0$인 쌍 $(i, j)$의 개수를 찾는 문제.2. 내 접근 방식Pythona, b = map(int, input().split())
my_list = list(map(int, input().split()))
sum_list = [0]*a
for i in range(a):
    for j in range(a):
        sum_list[i]+=my_list[j]
        print(sum_list)
a를 데이터 개수($N$), b를 나누는 수($M$)로 입력받음.이중 반복문을 사용하여 모든 구간의 합을 직접 계산하려고 시도함.3. 틀린 이유시간 복잡도 ($O(N^2)$): 문제에서 $N$은 최대 1,000,000입니다. 이중 반복문을 쓰면 $10^{12}$번 연산하게 되어 시간 초과가 발생합니다.구간 합 로직 오류: sum_list[i]에 단순히 my_list 전체를 더하는 방식은 특정 구간의 합을 나타내지 못합니다.메모리 및 출력: 루프 안에서 매번 리스트를 출력하면 출력 과부하로 프로그램이 멈출 수 있습니다.4. 올바른 접근 및 풀이💡 핵심 아이디어: 나머지 정리구간 $[i, j]$의 합이 $M$으로 나누어 떨어지려면:$$(S[j] - S[i-1]) \pmod M = 0 \implies S[j] \pmod M = S[i-1] \pmod M$$즉, 누적 합을 M으로 나눈 나머지 값이 같은 두 지점을 고르면, 그 사이 구간의 합은 반드시 M의 배수가 됩니다.✅ 최적화된 풀이 코드Pythonimport sys
input = sys.stdin.readline

# 1. 입력 받기
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 2. 누적 합과 나머지 카운트
prefix_sum = 0
remainder_count = [0] * m  # 나머지가 같은 인덱스의 개수를 저장
result = 0

for i in range(n):
    prefix_sum += numbers[i]
    remainder = prefix_sum % m
    
    # 나머지가 0이라면 그 자체로 하나가 성립
    if remainder == 0:
        result += 1
        
    # 같은 나머지를 가진 이전 위치들의 개수만큼 결과에 더함
    remainder_count[remainder] += 1

# 3. 나머지가 같은 것들 중에서 2개를 뽑는 조합(nC2) 계산
# S[j] % M == S[i-1] % M 인 경우를 찾는 과정
for count in remainder_count:
    if count >= 2:
        result += (count * (count - 1)) // 2

print(result)
5. 배운점
공백을 이용한 입력값 받기: map(int, input().split())을 통해 한 줄의 입력을 여러 변수나 리스트로 할당하는 법을 익힘.구간 합(Prefix Sum) 리스트: 리스트의 누적된 합을 미리 구해두면 $O(1)$의 속도로 구간 합을 구할 수 있음을 배움.나머지 연산의 성질: $(A-B) \pmod M = 0$이 $A \pmod M = B \pmod M$과 같다는 수학적 원리를 코딩 테스트에 적용하는 법을 깨달음.시간 복잡도 고려: $N$의 범위가 클 때는 $O(N^2)$이 아닌 $O(N)$의 알고리즘을 설계해야 함.