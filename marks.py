while True:
    print("\nMENU \n1.average marks \n2.absent students \n3.minimum marks \n4.maximum marks \n5.highest frequency marks ")
    list=[]
    list1=[]
    sum=0
    absent=0
    freq={}
    c=int(input("enter the choice :"))
    n=int(input("enter the total number of students : "))
    for i in range(1,n+1):
        score=input("enter the marks scored in fundamentals of data structure ")
        list.append(score)
    print(list)
    for i in list:
        if i.isalpha()==True:
            absent=absent+1
        else:
            i=int(i)
            sum=sum+i
    if c==1:
        avg=sum/(n-absent)
        print("the average of the marks scored is :",avg)
    elif c==2:
        print("the number of absent students ",absent)
    elif c==3:
        a=list.sort()
        print("the minimum marks scored are: ")
        print(list[0])
    elif c==4:
        for i in list:
            if i.isalpha()==False:
                list1.append(i)
        max_marks=max(list1)
        print("the maximum marks scored are : ",max_marks)
    elif c==5:
        for score in list:
            if score!=None:
                if freq.get(score)==None:
                    freq[score]=1
                else:
                    freq[score]+=1
        print(freq)
    else:
        print("invalid choice exiting the program ")
    cont = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
    if cont == 'yes':
            continue
    else:
        print("Exiting the program. Goodbye!")
        break
