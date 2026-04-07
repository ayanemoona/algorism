from collections import deque
N, L = map(int,input().split())
mydeque = deque();  # 덱 선언
now = list(map(int,input().split()))

for i in range(N):
    #아이디어 1 나보다 큰 데이터 삭제하기
    while mydeque and mydeque[-1][0] > noew [i]: # 맨 뒤 데이터 [0번째 값]
        mydeque.pop()
    mydeque.append((now[i],i)) #덱에 데이터 삽입 노드 추가 (값, 인덱스)
    # 슬라이딩 윈도우 벗어난 데이터 삭제 
    if mydeque[0][1] <= i-L : # 윈도우 범위를 벗어나면
        mydeque.popleft() # 맨 앞 데이터 삭제
    print(mydeque[0][0], end=' ') # 맨 앞 데이터 출력