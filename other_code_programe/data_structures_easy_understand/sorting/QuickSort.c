#include<stdio.h>

typedef struct
{
    int r[10001];
    int length;
}Sqlist;

void swap(Sqlist *L, int low, int high)
{
    int temp = L->r[low];
    L->r[low] = L->r[high];
    L->r[high] = temp;
}

int partition(Sqlist *L, int low, int high)
{
    int pivot=L->r[low-1];
    while(low<high)
    {
        while(low<high && L->r[high]>=pivot)    //把比枢轴记录小的记录交换到低端
            high--;
        swap(L, low, high);
        while(low<high && L->r[low]<=pivot)     //把比枢轴记录大的记录交换到高端
            low++;
        swap(L, low, high);
    }
    return low;     //返回枢轴所在位置
}

void QSort(Sqlist *L, int low, int high)
{
    int pivot;
    if(low<high) {
        pivot = partition(L, low, high);
        QSort(L, low, pivot-1);
        QSort(L, pivot+1, high);
    }
}

void QuickSort(Sqlist *L)
{ 
	QSort(L,0,L->length-1);
}

void print(Sqlist *L)
{
    int i;
    for(i=1; i<L->length; i++)
        printf("%d,", L->r[i]);
    printf("%d",L->r[i]);
    printf("\n");
}

  
#define N 9
int main(void)
{
    // int d[N]={50,10,90,30,70,40,80,60,20};
    int d[N] = {20,10,30,50,90,80,70,60,40};
    Sqlist l9;
    for(int i=0; i<N; i++) {
        l9.r[i] = d[i];
    }
    l9.length = N;

    printf("排序前：");
    for(int i=0; i<l9.length; i++) {
        printf("%d,", l9.r[i]);
    }
    printf("\n");

    printf("快速排序:");
    QuickSort(&l9);
    print(&l9);
    // for(int i=0; i<l9.length; i++) {
    //     printf("%d,", l9.r[i]);
    // }

    return 0;
}
