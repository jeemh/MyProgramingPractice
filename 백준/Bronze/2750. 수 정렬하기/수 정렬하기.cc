#include<stdio.h>
#include<stdlib.h>
#include <string.h>
#include<ctype.h>
#include<math.h>

void selection(int arr[],int n)
{
    int min,empty;
    for(int i=0;i<n-1;i++)
    {
        min = i;

        for(int j=i+1;j<n;j++)
        {
            if(arr[j]<arr[min])
                min = j;
        }

        empty = arr[i];
        arr[i] = arr[min];
        arr[min] = empty;
    }
}

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];

    for(int i=0;i<n;i++)
        scanf("%d",&arr[i]);

    selection(arr,n);

    for(int i=0;i<n;i++)
        printf("%d\n",arr[i]);
        
    return 0;
}