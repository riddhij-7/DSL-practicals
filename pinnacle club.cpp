#include <iostream>
#include <string>
using namespace std;

struct node {
    int prn;
    string name;
    node* next;
};

class list {
    node* head;

public:
    list() : head(NULL) {}

    node* create(int val, string n);
    void insertend();
    void insertat();
    void insertbeg();
    void display();
    void op();
    void concatenate(list &other);
    void del();
};

node* list::create(int val, string n) {
    node* temp = new node;
    if (temp == NULL) {
        cout << "Memory allocation failed" << endl;
        return NULL;
    } else 
	{
        temp->prn = val;
        temp->name = n;
        temp->next = NULL;
        return temp;
    }
}

void list::insertend() {
    int val;
    string n;
    cout << "Enter your PRN: ";
    cin >> val;
    cout << "Enter your name: ";
    cin.ignore();
    getline(cin, n);

    node* newNode = create(val, n);
    if (head == NULL) {
        head = newNode;
    } else {
        node* t = head;
        while (t->next != NULL) {
            t = t->next;
        }
        t->next = newNode;
    }
    cout << "Element has been inserted at the end" << endl;
}

void list::insertat() {
    int val, pos;
    string n;
    cout << "Enter the position where you want to insert: ";
    cin >> pos;
    cout << "Enter PRN: ";
    cin >> val;
    cout << "Enter Name: ";
    cin.ignore();
    getline(cin, n);

    if (pos == 1) {
        insertbeg();
    } else {
        node* t = head;
        int counter = 1;

        while (t != NULL && counter < pos - 1) {
            t = t->next;
            counter++;
        }

        if (t == NULL) {
            cout << "Position is out of scope." << endl;
        } else {
            node* newNode = create(val, n);
            newNode->next = t->next;
            t->next = newNode;
            cout << "Member Inserted at Position: " << pos << endl;
        }
    }
}

void list::insertbeg() {
    int val;
    string n;
    cout << "Enter your PRN: ";
    cin >> val;
    cout << "Enter your name: ";
    cin.ignore();
    getline(cin, n);

    node* newNode = create(val, n);
    newNode->next = head;
    head = newNode;
    cout << "President updated" << endl;
}

void list::display() {
    if (head == NULL) {
        cout << "List is empty" << endl;
        return;
    }

    node* temp = head;
    cout << "List: " << endl;

    int position = 1;
    while (temp != NULL) {
        if (position == 1) {
            cout << "President: ";
        }
		else if(temp->next==NULL)
		{
			cout<<"secretary :";
		} 
		else 
		{
            cout << "Member " << position - 1 << ": ";
        }
        cout << temp->prn << " - " << temp->name << endl;
        temp = temp->next;
        position++;
    }
}
void list::concatenate(list &other) {
    if (head == NULL) {
        head = other.head;
    } else {
        node* t = head;
        while (t->next != NULL) {
            t = t->next;
        }
        t->next = other.head;
    }
    // Clear the other list
    other.head = NULL;
    cout << "Lists have been concatenated." << endl;
    display();
}
void list::del()
{
	int r;
	cout<<"enter the prn of the member to be deleted :";
	cin>>r;
	if(head==NULL)
	{
		cout<<"list is empty ";
	}
	node* temp=head;
	node* prev=NULL;
	if(temp!=NULL && temp->prn==r)
	{
		head=temp->next;
		delete temp;
		cout<<"member with prn "<<r<<"is deleted "<<endl;
		return;
	}
	while(temp!=NULL && temp->prn!=r)
	{
		prev=temp;
		temp=temp->next;
		
	}
	if(temp==NULL)
	{
		cout<<"member with prn "<<r<<" not found "<<endl;
		return;	
	
	}	
	prev->next==temp->next;
	delete temp;
	cout<<"member with prn "<<r<<" was deleted";
	
}

void list::op() {
    while (true) {
        int choice;
        cout << "\nEnter: \n1. Add President \n2. Add Member at End \n3. Add Member at Position \n4. Display \n5. Concatenate with Another List \n6. Delete a Member \n7. Display concatenated list \n0. Exit" << endl;
        cin >> choice;
        switch (choice) {
            case 1:
                insertbeg();
                break;
            case 2:
                insertend();
                break;
            case 3:
                insertat();
                break;
            case 4:
                display();
                break;
            case 5:
                {
                    list otherList;
                    cout << "Enter details for the second list:" << endl;
                    otherList.op(); // Use the same menu for the second list
                    concatenate(otherList);
                }
                break;
            case 6:
            	del();
            	break;
            case 7:
            	cout<<"the concatenated list is ";
                continue;
            case 0:
            	return;
            	
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }
}

int main() {
    list listA, listB;
    int choice;

    while (true) {
        cout << "Enter: \n1. List A \n2. List B \n3. Concatenate Lists  \n0. Exit" << endl;
        cin >> choice;
        switch (choice) {
            case 1:
                cout << "\nList A:" << endl;
                listA.op();
                break;
            case 2:
                cout << "\nList B:" << endl;
                listB.op();
                break;
            case 3:
                listA.concatenate(listB);
                break;
            case 0:
                return 0;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    }
}
