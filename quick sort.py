percentage=[]
t=int(input("enter the total number of students :"))
for i in range(0,t):
    n=float(input("enter the percentage of students {0}: ".format(i+1)))
    percentage.append(n)
print("percentage of students are : ")
print(percentage)
def percentage_partition(percentage,start,end):
    pivot=percentage[start]
    lower_bound=start+1
    upper_bound=end
    while True:
        while lower_bound<=upper_bound and percentage[lower_bound]<=pivot:
            lower_bound+=1
        while lower_bound<=upper_bound and percentage[lower_bound]<=pivot:
            upper_bound-=1
        if lower_bound<=upper_bound:
            percentage[lower_bound],percentage[upper_bound]=percentage[upper_bound],percentage[lower_bound]
        else:
            break

    percentage[start],percentage[upper_bound]=percentage[upper_bound],percentage[start]
    return upper_bound

def Quick_sort(percentage,start,end):
    while start<end:
        partition=percentage_partition(percentage,start,end)
        Quick_sort(percentage,start,partition-1)
        Quick_sort(percentage,partition+1,end)
        return percentage 
sorted_percentage=Quick_sort(percentage,0,len(percentage)-1)
print("the list of perentages after performing quick sort ")
print(sorted_percentage)
def display_top_five(percentage):
    print("the top five percentages are ")
    if len(percentage)<5:
        start,stop=len(percentage)-1,-1
    else:
        start,stop=len(percentage)-1,len(percentage)-6
    for i in range(start,stop,-1):
        print(percentage[i],sep="\n")
a=input("do you want to display the top 5 percentages of students (yes/no): ")
if a=="yes ":
    display_top_five(sorted_percentage)
    print(display_top_five)
else:
    print("exiting the program")
