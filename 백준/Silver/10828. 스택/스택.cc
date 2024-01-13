#include<stdio.h>
#include<stdlib.h>
#include <string.h>
#include<ctype.h>
#include<math.h>
int number[100001];
int count = 0;
//push X: 정수 X를 스택에 넣는 연산
void push(int num) {
	number[count] = num;
	count++;
}
//pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
void pop() {
	if (count != 0) {
		count--;
		printf("%d\n", number[count]);
		number[count] = 0;
	}
	//만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
	else
		printf("%d\n", -1);

}
//top: 스택의 가장 위에 있는 정수를 출력
void top() {
	if (count != 0)
		printf("%d\n", number[count - 1]);
	//스택에 들어있는 정수가 없는 경우에는 - 1
	else
		printf("%d\n", -1);
}
//size: 스택에 들어있는 정수의 개수를 출력
void size() {
	printf("%d\n", count);
}
void empty() {
	//empty: 스택이 비어있으면 1
	if (count != 0) {
		printf("0\n");
	}
	//아니면 0을 출력
	else {
		printf("1\n");
	}
}
int main()
{
    int test,n;
    char comm[10];
    scanf("%d",&test);
    
    for(int i=0;i<test;i++)
    {
        scanf("%s",comm);
        if(strcmp(comm,"push")==0)
        {
            scanf("%d",&n);
            push(n);
        }
        else if(strcmp(comm,"pop")==0)
        {
            pop();
        }
        else if(strcmp(comm,"size")==0)
        {
            size();
        }
        else if(strcmp(comm,"empty")==0)
        {
            empty();
        }
        else if(strcmp(comm,"top")==0)
        {
            top();
        }
    }
    
    
    return 0;
}