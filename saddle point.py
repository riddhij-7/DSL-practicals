a=[]
n=int(input("enter the number of rows and columns"))
for i in range(n):
    b=[]
    for j in range(n):
        j=int(input("enter the number in pocket["+str(i)+"]["+str(j)+"]:"))
        b.append(j)
    a.append(b)
print("the matrix is:")
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
for i in range(n):
    min=a[i][0]
    c=0
    for j in range(n):
        if a[i][j]<min:
            min=a[i][j]
            c=j
    max=a[0][c]
    for k in range(n):
        if a[k][c]>max:
            max=a[k][c]
    if min==max:
        print("saddle point of matrix is ",min)
        f=1
if f==0:
    print("no saddle point")
    
