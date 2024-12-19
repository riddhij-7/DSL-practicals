print("\nMENU \n1.bubblesort \n2.selection sort ")
c=int(input("enter your choice:"))
list=[]
n=int(input("enter the number of values :"))
for i in range(1,n+1):
    value=int(input("enter the values :"))
    list.append(value)
print(list)
if c==1:
    for i in range(0,n):
        for j in range(0,n-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
            else:
                pass
    print("the sorted list is: ")
    print(list)
elif c==2:
    length=len(list)
    for i in range(0,length-1):
        min=i
        for j in range(i+1,length):
            if list[j]<list[min]:
                min=j
        list[i],list[min]=list[min],list[i]
    print("the sorted list")
    print(list)
else:
    print("you have entered the wrong choice")
