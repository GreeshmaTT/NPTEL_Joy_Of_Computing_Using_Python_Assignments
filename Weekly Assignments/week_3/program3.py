A=[int(i) for i in input().split(" ")]

for i in range(len(A)):
  if(A[i]%5!=0):
    print(A[i],end=" ")