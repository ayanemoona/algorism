lst = []
for i in range(9):
    a = int(input())
    lst.append(a)

lst.sort()

b = c = None  
found = False

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):  # i+1부터 시작해서 중복 제거
        if sum(lst) - lst[i] - lst[j] == 100:
            b, c = lst[i], lst[j]  
            found = True
            break
    if found:
        break


if b is not None and c is not None:  
    lst.remove(b)
    lst.remove(c)

for i in lst:
    print(i)
