N = int(input())
count=0
for i in range(666,99999999):
    if '666' in str(i):
        count+=1
    if N == count:
        print(i)
        break