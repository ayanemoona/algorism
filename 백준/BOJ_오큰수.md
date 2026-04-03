# [17298] 오큰수

- **문제 링크:** [https://www.acmicpc.net/problem/17298](https://www.acmicpc.net/problem/17298)
- **상태:** 비효율 (수정 중)
- **복습 필요:** Y

---

## 1. 문제 설명
크기가 $N$인 수열 $A = [A_1, A_2, \dots, A_N]$이 주어질 때, 각 원소 $A_i$에 대해 **오큰수(NGE, Next Greater Element)**를 구하는 문제입니다.오큰수의 정의:$A_i$의 오른쪽에 있으면서,$A_i$보다 큰 수 중에서,가장 왼쪽에 있는 수(즉, 가장 먼저 나타나는 큰 수)를 의미합니다.예외 사항: 그러한 수가 없는 경우 오큰수는 -1입니다.제약 조건: $N$이 최대 **1,000,000(백만)**이므로, 단순하게 $O(N^2)$으로 모든 우측 원소를 탐색하면 시간 초과가 발생합니다.



---

## 2. 내 접근 방식
```python
A = list(map(int,input().split()))
result = [0]*N
for i in range(N):
    for j in range(i+1,N):
         if A[i] < A[j]:
            result[i]=A[j]
            break
    if(result[i] == 0):
        result[i] = -1

print(*result)
```



---

## 3. 틀린 이유
- 그냥 시간 복잡도 생각 안하고 이중 for문 구조로 모든 요소를 훝어감


---

## 4. 올바른 접근 풀이





---

## 5. 배운점
