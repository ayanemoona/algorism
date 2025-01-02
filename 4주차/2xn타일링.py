def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if d[n] != 0 :  # 이미 계산한 적 있으면 그대로 반환
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)        # 아직 계산하지 않았으면 점화식에 의해 피보나치 결과 반환
    return d[n]

n=int(input())
d=[0]*(n+1)
print(fibo(n)%10007)
