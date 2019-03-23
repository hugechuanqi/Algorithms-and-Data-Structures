#include "stdio.h"  

/* 折半查找 */
int Binary_Search(int *a,int n,int key)     /*n表示长度，key表示查找值*/
{
	int low,high,mid;
	low=1;	/* 定义最低下标为记录首位 */
	high=n;	/* 定义最高下标为记录末位 */
	while(low<=high)
	{
		mid=(low+high)/2;	/* 折半 */
		if (key<a[mid])		/* 若查找值比中值小 */
			high=mid-1;		/* 最高下标调整到中位下标小一位 */
		else if (key>a[mid])/* 若查找值比中值大 */
			low=mid+1;		/* 最低下标调整到中位下标大一位 */
		else
		{
			return mid;		/* 若相等则说明mid即为查找到的位置 */
		}
		
	}
	return 0;
}

#define MAXSIZE 100 /* 存储空间初始分配量 */
int main(void)
{
    int arr[MAXSIZE]={0,1,16,24,35,47,59,62,73,88,99};

    int a[MAXSIZE],i, result;
    for(i=0;i<=MAXSIZE;i++)
	{
		a[i]=i;
	}

    result=Binary_Search(arr,10,16);
	printf("Binary_Search:%d \n",result);
}
