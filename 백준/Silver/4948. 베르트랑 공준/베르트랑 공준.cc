#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n,cnt;
    int arr[250000];
    
    for (int i=0;i<250000; i++)
        arr[i] = 1;
    
    arr[0] = arr[1] = 0;
    for(int i=2;i<=250000 ; i++)
        for(int j=i+i;j<=250000;j+=i)
            arr[j] = 0;
    
    while(1)
    {
        cnt=0;
        scanf("%d",&n);
        if(n==0)
            break;
        for(int i=n+1;i<=n*2;i++)
            if(arr[i])
                cnt++;
        printf("%d\n",cnt);
    }
        
    return 0;
}