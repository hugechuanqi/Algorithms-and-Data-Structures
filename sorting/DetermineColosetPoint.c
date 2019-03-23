#include<stdio.h>
#include<stdlib.h>

/* 折半查找 */
int Binary_Search(int *a,int n,float key)     /*n表示长度，key表示查找值*/
{
	int low,high,mid;
	low=0;
	high=n;
	while(low<=high)
	{
		mid=(low+high)/2;
		if (key<=a[mid])
			high=mid-1;
		else if (key>a[mid])
			low=mid+1;	
	}
	return low-1;  /*返回查找到值的较小坐标*/
}

int area(int x_Index, int y_Index)
{
    int x1,x2,y1,y2;
    x1 = x_Index-1; x1 = x_Index+1;
    y1 = y_Index-1; y1 = y_Index+1;

    return x1,x2,y1,y2;
}

int main()
{
    int arr[]={0,1,2,3,4,5,6,7,8,9};
    int *xArr = (int*)malloc(sizeof(int) * 10);
    int *yArr = (int*)malloc(sizeof(int) * 10);
    int xEndPoint[] = {3.7,3.8,3.9,4.1,4.2,4.3,4.4,4.5,4.6,4.6};
    int yEndPoint[] = {4.3,4.4,4.5,3.4,3.5,3.6,3.7,3.8,3.9,4.6};
    int numEndPoint = 11;

    for (int i=0; i<10;i++) {
        xArr[i] = arr[i];
    }
    for (int i=0; i<10;i++) {
        yArr[i] = arr[i];
    }

    float x,y;
    printf("请输入一个目标点横坐标：");
    scanf("%f",&x);
    printf("请输入一个目标点纵坐标：");
    scanf("%f",&y);
    int xIndex, yIndex, mapLength=10;
    xIndex = Binary_Search(xArr, mapLength, x);
    yIndex = Binary_Search(yArr, mapLength, y);
    // for(i=0; x>xArr[i] && i<10; i++); i--;
    // for(j=0; y>yArr[j] && j<10; j++); j--;

    printf("目标点所在网格位置为：(%d,%d)\n",xIndex,yIndex);

    int xmin,xmax,ymin,ymax;
    xmin,xmax,ymin,ymax = area(xIndex, yIndex);

    for(int i=0; i<numEndPoint; i++) {
        if(xmin<xEndPoint[i]<xmax && ymin<yEndPoint[i]<ymax)
            // xChoose 
         
    }


    return 0;
}



