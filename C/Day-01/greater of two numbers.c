#include<stdio.h>
int main(){
    int a;
    int b;
    scanf("%d %d",&a,&b);
    if (a>b)
    {
        printf("a is greater");
    }
    else if (b>a)
    {
        printf("b is greater");
    }
    else
    {
        printf("Both are equal");
    }
}
