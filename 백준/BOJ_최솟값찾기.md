# [11003] 최솟값 찾기

- **문제 링크:** [https://www.acmicpc.net/problem/11003](https://www.acmicpc.net/problem/11003)
- **상태:** 비효율 (수정 중)
- **복습 필요:** Y

---

## 1. 문제 설명
$N$개의 수 $A_1, A_2, \dots, A_N$이 주어집니다. 이때, $A_{i-L+1}$부터 $A_i$까지의 수 중에서 최솟값을 찾아 출력하는 문제입니다. ($i \le 0$인 $A_i$는 무시합니다.)

즉, 고정된 길이 $L$을 가진 **슬라이딩 윈도우(Sliding Window)**가 오른쪽으로 한 칸씩 이동할 때마다 그 윈도우 안에 포함된 숫자들 중 가장 작은 값이 무엇인지 매번 구해야 합니다. $N$과 $L$의 범위가 최대 5,000,000으로 매우 크기 때문에, 단순히 매번 구간을 검사하는 방식($O(N \times L)$)이 아닌 매우 효율적인 알고리즘이 필요합니다.



---

## 2. 내 접근 방식
```python
N,L = map(int,input().split())
A = list(map(int,input().split()))
result = []
for i in range(L-1):
    A.insert(0,5000000)
for i in range(N):
    min = 5000000
    for j in range(L):
        if(A[i+j] < min):
            min = A[i+j]
    result.append(min)
    
print(*result)
```



---

## 3. 틀린 이유
- 그냥 시간 복잡도 생각 안하고 정렬로 처리를 하려고 함 
- 최대값을 임의로 넣고 돌림 
- 방법을 다 모르고 있고 수동으로 리스트 잘라내서 함 


---

## 4. 올바른 접근 풀이
1. 최소값 가능성 없는 데이터 삭제
2. window 크기 값 데이터 삭제




---

## 5. 배운점
