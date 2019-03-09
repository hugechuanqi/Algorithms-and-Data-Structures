#include <stdio.h>
#

#define MaxSize 10000
typedef struct 
{
    int r[MaxSize+1];
    int length;
    /* data */
}Sqlist;

void swap(Sqlist *L, int i, int j)
{
    int temp = L->r[i];
    L->r[i]=L->r[j];
    L->r[j]=temp;
}

void print(Sqlist L)
{
    int i;
    for(i=1; i<L.length; i++)
        printf("%d,", L.r[i]);
    printf("%d",L.r[i]);
    printf("\n");
}

void InsertSort(SqList *L)
{ 
	int i,j;
	for(i=2;i<=L->length;i++)
	{
		if (L->r[i]<L->r[i-1]) /* 需将L->r[i]插入有序子表 */
		{
			L->r[0]=L->r[i]; /* 设置哨兵 */
			for(j=i-1;L->r[j]>L->r[0];j--)
				L->r[j+1]=L->r[j]; /* 记录后移 */
			L->r[j+1]=L->r[0]; /* 插入到正确位置 */
		}
	}
}

#define N 9
int main()
{
    int d[N] = {20,10,30,50,90,80,70,60,40};
    
    Sqlist l1;
    for(int i=0; i<N; i++)      //传递数组元素
        l1.r[i+1] = d[i];
    l1.length=N;                //传递数组长度
    
    printf("排序前：\n");
    print(l1);

    printf("冒泡排序\n");
    BubbleSort(&l1);
    print(l1);

    return 0;
}