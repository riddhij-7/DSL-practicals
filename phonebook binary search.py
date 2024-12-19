def recursive_binary_search(phonebook,name,low,high):
    if high>=low:
        mid=(low+high)//2
        if phonebook[mid][0]==name:
            return mid
        elif phonebook[mid][0]>name:
            return recursive_binary_search(phonebook,name,low,mid-1)
        else:
            return recursive_binary_search(phonebook,name,mid+1,high)
    return-1
def non_recursive_binary_search(phonebook,name):
    low=0
    high=len(phonebook)-1
    while low<=high:
        mid=(low+high)//2
        if phonebook[mid][0]==name:
            return mid
        elif phonebook[mid][0]>name:
            high=mid-1
        else:
            low=mid+1
    return-1
def get_name(item):
    return item[0]
def insert_friend(phonebook,name,mobile_number):
    if not phonebook:
        phonebook.append((name,mobile_number))
        return
    index=non_recursive_binary_search(phonebook,name)
    if index!=-1:
        print("friend already exists in the phonebook")
    else:
        phonebook.append((name,mobile_number))
        phonebook.sort(key=get_name)
        print(f"friend{name} inserted successfully")
def display_menu():
    print("\nPhonebook Menu ")
    print("\n1.add friend \n2.Search friend \n3.display all friends \n4.exit")
def main():
    phonebook=[]
    while True:
        display_menu()
        choice=int(input("enter your choice(1-4): "))
        if choice==1:
            name=input("enter a friends name: ").strip()
            mobile_number=input("enter friend's mobile number: ").strip()
            insert_friend(phonebook,name,mobile_number)
        elif choice==2:
            name=input("enter friends name that is to be searched ")
            index=non_recursive_binary_search(phonebook,name)
            if index!=-1:
                print(f"friend found: name={phonebook[index][0]},mobile number={phonebook[index][1]}")
            else:
                print("friend not found in the phonebook ")
        elif choice==3:
            if not phonebook:
                print("phonebook is empty")
            else:
                print("phonebook:")
                for friend in phonebook:
                    print(f"name={friend[0]},mobile number={friend[1]}")
        elif choice==4:
            print("exiting the program ")
            break 
        else:
            print("invalid choice. please enter a valid number ")
if __name__=="__main__":
    main()
