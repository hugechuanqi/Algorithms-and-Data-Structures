#include <stdio.h>
#

#define MaxSize 10000
typedef struct 
{
    int r[MaxSize+1];
    int length;
    /* data */
}Sqlist;

void swap(Sqlist L, int i, int j)
{
    int temp = L.r[i];
    L.r[i]=L.r[j];
    L.r[j]=temp;
}

void print(Sqlist *L)
{
    int i;
    for(i=1; i<L->length; i++)
        printf("%d,", L->r[i]);
    printf("%d",L->r[i]);
    printf("\n");
}

void BubbleSort(Sqlist L)
{
    for(int i=1; i<L.length; i++)
    {
        for(int j=L.length-1; j>=i; j--)
        {
            if(L.r[j] > L.r[j+1])
            {
                swap(L, j, j+1);
            }
        }
    }
}

#define N 9
int main()
{
    int d[N] = {20,10,30,50,90,80,70,60,40};
    
    Sqlist l0;
    for(int i=0; i<N; i++)      //传递数组元素
        l0.r[i+1] = d[i];
    l0.length=N;                //传递数组长度
    
    printf("排序前：\n");
    print(&l0);

    printf("冒泡排序\n");
    BubbleSort(l0);
    print(&l0);

    return 0;
}