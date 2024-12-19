#include<iostream>
#include<string.h>
#define max 50
using namespace std;
class stack
{
	public:
		char a[max];
		int top;
	public:
		stack()
		{
			top=-1;
		}
		void push(char);
		void reverse();
		void convert(char[]);
		void palindrome();
};
void stack::push(char c)
{
	top++;
	a[top]=c;
	a[top+1]='\0';
	cout<<endl<<c<<" is pushed into the stack...";
	
}
void stack::reverse()
{
	char str[max];
	cout<<"\n\n reverse string is : ";
	for (int i=top,j=0;i>=0;i--,j++)
	{
		cout<<a[i];
		str[j]=a[i];
		
	}
	cout<<endl;
}
void stack::convert(char str[])
{
	int j,k,len=strlen(str);
	for(j=0,k=0;j<len;j++)
	{
		if(((int)str[j]>=97 && (int)str[j]<=122)||((int)str[j]>=65 && (int)str[j]<=90))
		{
			if((int)str[j]<=90)
			{
				str[k]=(char)((int)str[j]+32);
				
			}else{
				str[k]=str[j];
			}
			k++;
		}
	}str[k]='\0';
	cout<<endl<<"converted string "<<str<<"\n";
	
}
void stack::palindrome()
{
	char str[max];
	int i,j;
	for(i=top,j=0;i>=0;i--,j++)
	{
		str[j]=a[i];
	}
	str[j]='\0';
	if(strcmp(str,a)==0)
	cout<<"\n\n string is palindrome ";
	else
	cout<<"\n\n string is not palindrome";
}
int main()
{
	stack s;
	char str[max];
	int i=0;
	cout<<"\n enter string to be reversed and check if it is a palindrome or not";
	cin.getline(str,50);
	s.convert(str);
	while(str[i]!='\0')
	{
		s.push(str[i]);
		i++;
	}
	s.palindrome();
	s.reverse();
}
