a=int(input())
lst=[1,0,0]
cup=0
for i in range(a):
    b,c=map(int,input().split())
    cup=lst[b-1]
    lst[b-1]=lst[c-1]
    lst[c-1]=cup
index = lst.index(1)
print(index+1)
