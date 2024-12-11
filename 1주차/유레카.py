triangle_number = [n*(n+1)//2 for n in range(1, 45)]
eureka = [0 for i in range(1001)]
for i in triangle_number:
    for j in triangle_number:
        for k in triangle_number:
            if i+j+k <= 1000:
                eureka[i+j+k] = 1
for i in range(int(input())):
    print(eureka[int(input())])