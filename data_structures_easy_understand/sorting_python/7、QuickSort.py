class Solution:
    def partition(self, Arr,low,high):
        hp = Arr[high]  #首先以hp为枢轴
        i = low - 1
        for j in range(low,high):
            if Arr[j] < hp:     #把比枢轴小的放到左边，枢轴实际位置就在i+1
                i = i+ 1
                (Arr[i], Arr[j]) = (Arr[j], Arr[i])
        (Arr[i+1], Arr[high]) = (Arr[high],Arr[i+1])    #确定枢轴位置后，再把枢轴值hp换过来
        return i+1  #返回枢轴值hp所在的位置

    def partition2(self, Arr, low, high):
        hp = Arr[high]
        while(low<high):
            while(low<high and Arr[low]<=hp):
                low += 1
            (Arr[low],   Arr[high]) = (Arr[high], Arr[low])
            while(low<high and Arr[high]>=hp):
                high -= 1
            (Arr[low], Arr[high]) = (Arr[high], Arr[low])
        return high

    def QuickSort(self, Arr, low, high):
        if low < high:
            pivot = self.partition2(Arr,low,high)
            self.QuickSort(Arr,low,pivot-1)
            self.QuickSort(Arr,pivot+1,high)
        return Arr


s = [5, 0, 1, 3, 6, 2, 4, 9, 12, 11, 18, 20, 7, 8, 19, 13, 14, 17, 16, 10]
a = Solution()
print("快速排序前：", s)
a.QuickSort(s,0,len(s)-1)
print("快速排序后:", s)
