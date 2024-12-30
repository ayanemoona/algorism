N=int(input())
score=[0,1]
for i in range(N-1):
    A=score[i]+score[i+1]
    score.append(A)
print(score[-1])