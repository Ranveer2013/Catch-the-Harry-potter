import random
A=[[1,2],[3,4]]
for i in A:
    for j in i:
        print(j)

print(A[0][0])

B=[]
for i in range(2):
    temp=[]
    for j in range(2):
        temp.append(random.randint(1,9))

    B.append(temp)

print(B)